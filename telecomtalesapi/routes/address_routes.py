from flask_restx import Resource
from flask_restx import fields
from flask_restx import reqparse
from flask import Response
from flask import request, jsonify
from telecomtalesapi import address_ns
from telecomtalesapi import db
from telecomtalesapi.models.address import Address
from telecomtalesapi.schemas import AddressSchema
from marshmallow import ValidationError
import xmltodict
from telecomtalesapi.auth import auth
from ..utils.api_utils import is_request_xml, should_return_xml, to_xml

# Define the model for Address input
address_model = address_ns.model('Address', {
    'streetNo': fields.String(required=True, description='The street number'),
    'street': fields.String(required=True, description='The street name'),
    'city': fields.String(required=True, description='The city'),
    'post': fields.String(required=True, description='The post district'),
    'postNo': fields.Integer(required=True, description='The post number')
})

# Create a request parser for query parameters
query_parser = reqparse.RequestParser()
query_parser.add_argument('streetNo', type=str, help='Street Number')
query_parser.add_argument('street', type=str, help='Street Name')
query_parser.add_argument('city', type=str, help='City')
query_parser.add_argument('post', type=str, help='Post District')
query_parser.add_argument('postNo', type=int, help='Post Number')

@address_ns.route('/') # Define route at the namespace level
class AddressList(Resource):
    @auth.login_required
    def get(self):
        # Retrieve all addresses
        addresses = Address.query.all()
        addresses_dict = [address.to_dict() for address in addresses]
        
        if should_return_xml():
            xml_data = to_xml({'addresses': addresses_dict})
            return Response(xml_data, mimetype='application/xml')
        else:
            return jsonify(addresses_dict)

    @auth.login_required
    @address_ns.expect(address_model, validate=True)
    def post(self):
        # Create a new address
        schema = AddressSchema()
        try:
            # Check if the request is XML
            if is_request_xml():
                data = schema.load(xmltodict.parse(request.data)['address'])
                address = Address(**data)
                db.session.add(address)
                db.session.commit()
                xml_data = to_xml({'address': address.to_dict()})
                return xml_data, 201, {'Content-Type': 'application/xml'}
            else:
                data = schema.load(request.json)
                existing_address = Address.query.filter_by(**data).first()
                if existing_address:
                    return {'message': 'Address with these details already exists'}, 400
                            
                address = Address(**data)
                db.session.add(address)
                db.session.commit()
                return address.to_dict(), 201
        except ValidationError as err:
            err_data = {'error': err.messages}
            if should_return_xml():
                xml_error = to_xml(err_data)
                return xml_error, 400, {'Content-Type': 'application/xml'}
            else:
                return err_data, 400

@address_ns.route('/<int:id>')  # Route for specific address by ID
class AddressResource(Resource):
    @auth.login_required
    @address_ns.expect(address_model, validate=True)
    def put(self, id):
        # Get a specific address by ID
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404

        if should_return_xml():
            return to_xml({'address': address.to_dict()}), 200, {'Content-Type': 'application/xml'}
        else:
            return address.to_dict(), 200

    @auth.login_required
    @address_ns.expect(address_model, validate=True)
    def put(self, id):
        # Update a specific address by ID
        schema = AddressSchema(partial=True)
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404

        try:
            data = schema.load(request.json) if not is_request_xml() else xmltodict.parse(request.data)['address']
            for key, value in data.items():
                setattr(address, key, value)
            db.session.commit()

            if should_return_xml():
                return to_xml({'address': address.to_dict()}), 200, {'Content-Type': 'application/xml'}
            else:
                return address.to_dict(), 200
        except ValidationError as err:
            if should_return_xml():
                return to_xml({'error': err.messages}), 400, {'Content-Type': 'application/xml'}
            else:
                return err.messages, 400

    @auth.login_required
    def delete(self, id):
        # Delete a specific address by ID
        address = Address.query.get(id)
        if not address:
            return {'message': 'Address not found'}, 404
        db.session.delete(address)
        db.session.commit()
        return '', 204

@address_ns.route('/query')
class AddressQuery(Resource):
    @auth.login_required
    @address_ns.expect(query_parser)  # Document query parameters
    def get(self):
        
        #Query addresses based on different parameters such as street, city, etc.
        
        args = query_parser.parse_args()  # Parse query parameters
        query = Address.query

        for key, value in args.items():
            if value and hasattr(Address, key):
                query = query.filter(getattr(Address, key) == value)

        addresses = query.all()

        if should_return_xml():
            return to_xml({'addresses': [address.to_dict() for address in addresses]}), 200, {'Content-Type': 'application/xml'}
        else:
            return jsonify([address.to_dict() for address in addresses])

@address_ns.route('/<int:address_id>/services')  # Route for listing services of a specific address
class AddressServices(Resource):
    @auth.login_required
    def get(self, address_id):
        # Retrieve services linked to a specific address
        address = Address.query.get(address_id)
        if not address:
            return {'message': 'Address not found'}, 404
        services = address.services.all()

        if should_return_xml():
            return to_xml({'services': [service.to_dict() for service in services]}), 200, {'Content-Type': 'application/xml'}
        else:
            return jsonify([service.to_dict() for service in services])
