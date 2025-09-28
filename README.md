# py_rest_swagger_example

A simple FastAPI CRUD app with SQLite and Swagger UI, Docker-ready.

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload