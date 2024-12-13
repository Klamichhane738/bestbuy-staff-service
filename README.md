# Flask REST API for Staff Management

This project demonstrates a REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on staff data, which can be tested locally and deployed to Azure App Service for cloud hosting.

## Features

- **Retrieve all staff members**: Get a list of all staff.
- **Retrieve a specific staff member by ID**: Fetch details of a staff member by their unique ID.
- **Create a new staff member**: Add a new staff record.
- **Update an existing staff member**: Modify details of an existing staff member by ID.
- **Delete a staff member**: Remove a staff record by ID.

## Prerequisites

Before you can run or deploy this app, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package manager)
- **Flask** (Install using `pip install Flask`)
- **gunicorn** (Install using `pip install gunicorn`)
- **Azure CLI** (optional, for deployment to Azure)

## Project Structure

- **app.py**: Main Flask application for handling API requests.
- **requirements.txt**: List of Python dependencies needed for the project.
- **test-api.http**: File for testing the REST API endpoints using the REST Client extension in Visual Studio Code.
- **README.md**: Documentation for the project.

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/bestbuy-staff-service.git
2. Navigate to the project directory:
```bash
cd bestbuy-staff-service
```
3. Install the dependencies:

pip install -r requirements.txt

4. Run the application:
python app.py

5. The API will be running at http://127.0.0.1:8000

Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.

### API Endpoints
GET /: Root endpoint with a welcome message.
GET /health: Health check endpoint to confirm the service is running.
GET /staff: Retrieve all staff members.
GET /staff/<id>: Retrieve a specific staff member by ID.
POST /staff: Add a new staff member.
PUT /staff/<id>: Update an existing staff member.
DELETE /staff/<id>: Delete a staff member.