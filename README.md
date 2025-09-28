# py_rest_swagger_example

## A simple FastAPI CRUD app with SQLite and Swagger UI, Docker-ready.
```bash
docker build --no-cache -t py-rest-swagger-example:latest .
docker run -p 8000:8000 -v $(pwd)/data:/app/data py-rest-swagger-example:latest
```

## Run locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

