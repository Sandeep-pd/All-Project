from pathlib import Path
import sqlite3
from contextlib import closing
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from database import Database


DB_PATH = Path(__file__).with_name("hospital.db")
db = Database(str(DB_PATH))
app = FastAPI(title="Hospital Management API", version="1.0.0")


class PatientCreate(BaseModel):
    patient_id: int = Field(gt=0)
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=150)
    gender: str = Field(min_length=1)
    phone: str | None = None
    disease: str | None = None


class DoctorCreate(BaseModel):
    doctor_id: int = Field(gt=0)
    name: str = Field(min_length=1)
    specialization: str = Field(min_length=1)
    phone: str | None = None


def row_to_dict(row: sqlite3.Row) -> dict:
    return dict(row)


@app.get("/health")
def health_check() -> dict:
    with closing(db.connect()) as connection:
        connection.execute("SELECT 1")
    return {"status": "ok", "database": "connected"}


@app.get("/patients")
def list_patients(
    patient_id: Annotated[int | None, Query(gt=0)] = None,
) -> list[dict]:
    with closing(db.connect()) as connection:
        connection.row_factory = sqlite3.Row
        if patient_id is None:
            rows = connection.execute(
                "SELECT patient_id, name, age, gender, phone, disease "
                "FROM patients ORDER BY patient_id"
            ).fetchall()
        else:
            rows = connection.execute(
                "SELECT patient_id, name, age, gender, phone, disease "
                "FROM patients WHERE patient_id = ?",
                (patient_id,),
            ).fetchall()
    return [row_to_dict(row) for row in rows]


@app.post("/patients", status_code=201)
def create_patient(patient: PatientCreate) -> dict:
    try:
        with closing(db.connect()) as connection, connection:
            connection.execute(
                "INSERT INTO patients "
                "(patient_id, name, age, gender, phone, disease) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    patient.patient_id,
                    patient.name,
                    patient.age,
                    patient.gender,
                    patient.phone,
                    patient.disease,
                ),
            )
            connection.row_factory = sqlite3.Row
            row = connection.execute(
                "SELECT patient_id, name, age, gender, phone, disease "
                "FROM patients WHERE patient_id = ?",
                (patient.patient_id,),
            ).fetchone()
    except sqlite3.IntegrityError as error:
        raise HTTPException(status_code=409, detail="Patient ID already exists") from error
    return row_to_dict(row)


@app.get("/doctors")
def list_doctors() -> list[dict]:
    with closing(db.connect()) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT doctor_id, name, specialization, phone "
            "FROM doctors ORDER BY doctor_id"
        ).fetchall()
    return [row_to_dict(row) for row in rows]


@app.post("/doctors", status_code=201)
def create_doctor(doctor: DoctorCreate) -> dict:
    try:
        with closing(db.connect()) as connection, connection:
            connection.execute(
                "INSERT INTO doctors (doctor_id, name, specialization, phone) "
                "VALUES (?, ?, ?, ?)",
                (
                    doctor.doctor_id,
                    doctor.name,
                    doctor.specialization,
                    doctor.phone,
                ),
            )
            connection.row_factory = sqlite3.Row
            row = connection.execute(
                "SELECT doctor_id, name, specialization, phone "
                "FROM doctors WHERE doctor_id = ?",
                (doctor.doctor_id,),
            ).fetchone()
    except sqlite3.IntegrityError as error:
        raise HTTPException(status_code=409, detail="Doctor ID already exists") from error
    return row_to_dict(row)
