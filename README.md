# TelecomTalesAPI

## Introduction
TelecomTalesAPI is a RESTful API developed using Flask for managing telecom services. It's designed as a lightweight solution for simulating telecommunication operator services.

## Features
- CRUD operations for Address and Service entities.
- Support for both JSON and XML data formats.
- Basic authentication.
- SQLite database integration.

## Setup Instructions


### Prerequisites
- Python 3
- pip (Python package installer)

### Installing Dependencies - (or skip to pip install -r requirements.txt)

1. **pip Installation**
   ```shell
   sudo apt install python3-pip

2. **Flask and Related Libraries**
   ```shell
   pip install Flask Flask-RESTful Flask-SQLAlchemy flask-httpauth Flask-Migrate

3. **Werkzeug Library**
   ```shell
   pip install Werkzeug

## Using Using requirements.txt

0. **To install all dependencies at once:**
   ```shell
   pip install -r requirements.txt


### Set up the database:
4. **Set up the database:**
   ```shell
   export FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade

## API Testing Tool

5. **Postman**
   ```shell
   snap install postman

## Flask-RESTX to generate OpenAPI documentation
6. **To use Flask-RESTX install:**
   ```shell
   pip install flask-restx

### In case of problems during "flask db init" step, run this:
6. **To use Flask-RESTX install:**
   ```shell
   pip install --upgrade flask-restx

## Scripts

7. **To use scripts install requests library**
   ```shell
   pip install requests

## Navigate to script folder and run script 

8. **To use script run paython script_name.py**
   ```shell
   python create_user_script.py

- `create_user_script.py`: Register a new user for accessing the API.
- `create_address_script.py`: Add a new address to the database.
- `create_service_script.py`: Create a new service associated with an address.
- `delete_address_script.py`: Remove an existing address from the database.
- `delete_service_script.py`: Delete a service from the database.
- `get_address_script.py`: Retrieve details of a specific address.
- `get_service_script.py`: Fetch details of a particular service.
- `update_address_script.py`: Update information for an existing address.
- `update_service_script.py`: Modify details of an existing service.
  
## Using the Flask-RESTX API

This project utilizes Flask-RESTX to organize and manage the RESTful API endpoints. Flask-RESTX provides an easy-to-use interface for both creating and documenting your API. Here’s how to interact with it:

### Getting Started

6. **Install Dependencies:**

   Make sure to install Flask-RESTX alongside Flask as previously stated:
   ```shell
   pip install flask-restx



6. **Run the aplications by starting the Flask application:**

   ```shell
   flask run

## Available Endpoints
The API is structured into namespaces, which group related endpoints. The following namespaces are available:


- `/addresses': Operations related to address entities.
- `/services': Operations for service entities.
- `/users': User-related operations.

## Accessing Endpoints
You can access the API endpoints using tools like curl or Postman. For example:

   '''shell
   curl -u username:password -X GET http://localhost:5000/addresses/

This command retrieves all addresses if you replace username:password with valid credentials.
Do note taht username:password should be some user and password of that user that is in the database

## Documentation
Flask-RESTX automatically generates Swagger documentation for all endpoints. Visit http://localhost:5000/ to view the interactive documentation and test the API directly from your browser.

## Authentication
The API uses HTTP Basic Authentication. Ensure you pass the correct username and password headers with each request that requires authentication.

For a more detailed guide on how to use each endpoint, refer to the auto-generated Swagger documentation provided by Flask-RESTX.

## Docker Implementation

### Docker Installation Guide
Follow these steps to install Docker on your Ubuntu system:

1. **Update the package list:**

   ```shell
   sudo apt-get update

2. **Install packages to allow apt to use a repository over HTTPS:**

   ```shell
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

3. **Add Docker’s official GPG key:**

   ```shell
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


4. **Set up the stable Docker repository:**

   ```shell
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

5. **Update the package list again:**

   ```shell
   sudo apt-get update

6. **Install containerd.io:**

   ```shell
   sudo apt-get install containerd.io

7. **Install Docker CE:**

   ```shell
   sudo apt-get install docker-ce
Install containerd.io and Docker CE:

8. **Test your Docker installation by running the hello-world image:**
   ```shell
   sudo docker run hello-world

This will download a test image and run it in a container. If you see a welcome message, Docker has been successfully installed.

## How to run the project in docker


1. **Build the project:**
   ```shell
   docker build -t telecomtalesapi .


2. **To run in docker:**
   ```shell
   docker run -p 5000:5000 telecomtalesapi

3. **To get CONTAINER ID:**
   ```shell
   docker ps

4. **To get access container shell :**
   ```shell
   docker exec -it [container_id_or_name] /bin/bash

Example:
container ID 86e7d7088027

4. **To get access container shell :**
   ```shell
   docker exec -it 86e7d7088027 /bin/bash

5. **Set up the database:**
   ```shell
   export FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade

5.  **Alternatively set up the database via script:**
   ```shell
   cd scripts/database_scripts
   python database_initialization_script.py 
