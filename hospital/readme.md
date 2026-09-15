Hospital Management API
=======================

Install the dependencies:

	pip install -r requirements.txt

Start the API from this directory:

	uvicorn api:app --reload

Run with Docker:

	docker build -t hospital-api .
	docker run --rm -p 8000:8000 hospital-api

The API is available at http://127.0.0.1:8000. Open http://127.0.0.1:8000/docs for the interactive API documentation.

Endpoints:

- GET /health checks the SQLite database connection.
- GET /patients lists patients, or filters by patient_id.
- POST /patients adds a patient.
- GET /doctors lists doctors.
- POST /doctors adds a doctor.

