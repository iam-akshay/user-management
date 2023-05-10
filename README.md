# User Management
A simple Django App using docker

## Requirements
- Docker
- Docker Compose

## Technologies Used
- Python (Django)
- Postgresql

## Running the application
To run the application, follow these steps:

- Clone the repository to your local machine.
- In the project directory, run `docker-compose up --build -d` command.
- Wait for the containers to start. You can monitor the logs using `docker-compose logs -f` command.
- Open your web browser and navigate to http://localhost:8000.
- That's it! The application should now be running in your browser.

## Stopping the application
To stop the application, run `docker-compose down -v` command in the project directory. This will stop and remove all the containers, networks, and volumes created by docker-compose up command.

## Endpoints:

### GET: /users/
Retrieves all users from the database.

### POST: /users/
Creates a new user.

**Parameters:**

- email (required): The email of the user.
- password (required): The password of the user.
- is_admin (optional): Whether the user is an administrator (default: False).
- is_staff (optional): Whether the user is staff (default: False).

### GET: /users/{id}/
Retrieves a particular user based on their ID.

**Parameters:**
- id (required): The ID of the user to retrieve.

### DELETE: /users/{id}/
Deletes a particular user based on their ID.

**Parameters:**
- id (required): The ID of the user to delete.
