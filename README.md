# Dropbox-like File Storage Service

This project is a simplified Dropbox-like service implemented using Django and Django REST Framework. It provides RESTful APIs for file upload, retrieval, update, deletion, and listing.

## Prerequisites

- Python 3.8+
- pip (Python package installer)

## Setup

1. Clone the repository:
2. git clone https://github.com/Suvodeep-13/typeface.git
3. cd dropbox_clone
4. Create a virtual environment: python -m venv venv
5. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
6. Install the required packages: pip install Django djangorestframework
7. Apply database migrations:
  ```
  python manage.py makemigrations
  ```
  ```
  python manage.py migrate
  ```
8. Run the development server: python manage.py runserver

### File Upload (Using Postman)

1. Set the HTTP method to POST
2. Enter the URL: `http://localhost:8000/files/upload/`
3. Go to the "Body" tab
4. Select "form-data"
5. Add two key-value pairs:
- Key: "file", Value: Select "File" from the dropdown and choose your file
- Key: "name", Value: Enter the name you want to give the file
6. Click "Send"

### Read File

Send a GET request to `http://localhost:8000/files/{fileId}/`, replacing `{fileId}` with the actual file ID.

### Update File

Send a PUT request to `http://localhost:8000/files/{fileId}/`, replacing `{fileId}` with the actual file ID. Use form-data to include the updated file and/or name.

### Delete File

Send a DELETE request to `http://localhost:8000/files/{fileId}/`, replacing `{fileId}` with the actual file ID.

### List Files

Send a GET request to `http://localhost:8000/files/`

## File Storage

Files are stored locally in the `media/uploads/` directory. In a production environment, you might want to use a cloud storage solution.
