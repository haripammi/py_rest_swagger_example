# py_rest_swagger_example

A simple FastAPI CRUD application with a MySQL database backend and Swagger UI. The application is also Docker-ready.

## Functional Specification

This application provides a RESTful API for Create, Read, Update, and Delete (CRUD) operations on a collection of "items".

### Data Model

An `item` has the following structure:
- `id`: A unique integer identifier (auto-generated).
- `name`: A string representing the name of the item (required).
- `description`: An optional string describing the item.

### API Endpoints

The following endpoints are available:

- **Create an item**
  - `POST /items/`
  - **Request Body**: A JSON object with `name` (string) and optional `description` (string).
  - **Response**: The newly created item object, including its `id`.

- **Read all items**
  - `GET /items/`
  - **Response**: A list of all item objects.

- **Read a single item**
  - `GET /items/{item_id}`
  - **Response**: The item object corresponding to the given `item_id`. Returns a 404 error if not found.

- **Update an item**
  - `PUT /items/{item_id}`
  - **Request Body**: A JSON object with updated `name` and/or `description`.
  - **Response**: The updated item object.

- **Delete an item**
  - `DELETE /items/{item_id}`
  - **Response**: A confirmation message.

The API includes a Swagger UI, available at `/docs` on the server root, for interactive testing and documentation.

## Design Specification

- **Framework**: Built with [FastAPI](https://fastapi.tiangolo.com/), a modern, high-performance web framework for building APIs with Python.
- **Database**: Uses a [MySQL](https://www.mysql.com/) database for data persistence.
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) is used as the Object-Relational Mapper to interact with the database.
- **Async Support**: The [databases](https://www.encode.io/databases/) library is used to provide asynchronous support for database operations.
- **Data Validation**: [Pydantic](https://pydantic-docs.helpmanual.io/) models are used for data validation, serialization, and automatic generation of the API schema.
- **Containerization**: The application is designed to be built and run as a [Docker](https://www.docker.com/) container.

## Dependencies

The application requires the following Python packages:
- `fastapi`
- `uvicorn[standard]`
- `sqlalchemy`
- `databases`
- `pydantic`
- `aiomysql`
- `PyMySQL`

## How to Run

### Running with Docker

1.  **Build the Docker image:**
    ```bash
    docker build --no-cache -t py-rest-swagger-example:latest .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 py-rest-swagger-example:latest
    ```
    The application will be available at `http://localhost:8000`.

### Running Locally

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    Before running, make sure to update the `DATABASE_URL` in `app/main.py` with your MySQL connection details.
    ```bash
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://localhost:8000`.