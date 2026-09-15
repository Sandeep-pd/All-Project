# 🏥 Hospital Management System (Python OOP Project)

## 📌 Project Overview

This is a simple **Hospital Management System** built using **Python Object-Oriented Programming (OOP)** concepts. The project manages patients, doctors, appointments, and billing information.

The system demonstrates real-world healthcare management operations such as:

* Patient Registration
* Doctor Management
* Appointment Booking
* Patient Visit History
* Bill Generation

---

## 🚀 Features

### 👨‍⚕️ Patient Management

* Store patient information
* Track patient visit history
* View complete patient details

### 🩺 Doctor Management

* Store doctor information
* Manage specialization details
* Display available appointment slots

### 📅 Appointment Booking

* Book appointments with doctors
* Check slot availability
* Display appointment confirmation details

### 💰 Billing System

* Calculate total bill amount
* Include:

  * Doctor Fee
  * Medicine Charges
  * Lab Charges
* Display billing details

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* datetime Module

---

## 📂 Project Structure

```text
hospital_management_system.py

├── Patient Class
├── Doctor Class
├── HospitalSystem Class
├── Bill Class
└── Main Program
```

---

## 📖 OOP Concepts Used

### Classes and Objects

* Patient
* Doctor
* HospitalSystem
* Bill

### Encapsulation

Patient, doctor, and billing data are stored inside objects.

### Composition

The Patient class uses the Bill object to calculate visit expenses.

### Methods

* visit_patient()
* get_patient_details()
* get_doctor_details()
* request_appointment()
* calculate_total()
* bill()

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/hospital-management-system.git
```

2. Navigate to the project folder

```bash
cd hospital-management-system
```

3. Run the Python file

```bash
python hospital_management_system.py
```

---

## 📊 Sample Output

```text
visit added

Id: 101
Name: sandeep
Age: 22

----patient history----
Disease : Fever
Doctor  : Dr Raj
Date    : 10-05-2026
Medicine: Paracetamol
Bill    : 1000

Appointment Confirmed
patient: sandeep
doctor: Dr Raj
date: monday
time: 10am
```

---

## 🔮 Future Improvements

* Store data using SQLite Database
* Add Login and Authentication
* GUI using Tkinter or PyQt
* Export Bills to PDF
* Multiple Doctor Scheduling
* Appointment Cancellation
* Patient Search Functionality

---

## 👨‍💻 Author

**Sandeep**

Python | Data Science | GenAI | Agentic AI Enthusiast

---

## ⭐ GitHub

If you found this project useful, please give it a ⭐ on GitHub.

## 🧪 API Testing with Postman

The Hospital Management API can be tested using **Postman**.

### 1. Start the FastAPI Server

Run the following command from the project directory:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

You can also open the automatic Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

### 2. Health Check

**Method:** `GET`

**Endpoint:**

```text
GET http://127.0.0.1:8000/health
```

**Expected Response:**

```json
{
    "status": "ok",
    "database": "connected"
}
```

---

### 3. Create a Patient

**Method:** `POST`

**Endpoint:**

```text
POST http://127.0.0.1:8000/patients
```

In Postman:

**Body → raw → JSON**

```json
{
    "patient_id": 1,
    "name": "Rahul Sharma",
    "age": 35,
    "gender": "Male",
    "phone": "9876543210",
    "disease": "Fever"
}
```

**Expected Response:**

```json
{
    "patient_id": 1,
    "name": "Rahul Sharma",
    "age": 35,
    "gender": "Male",
    "phone": "9876543210",
    "disease": "Fever"
}
```

---

### 4. Get All Patients

**Method:** `GET`

**Endpoint:**

```text
GET http://127.0.0.1:8000/patients
```

**Expected Response:**

```json
[
    {
        "patient_id": 1,
        "name": "Rahul Sharma",
        "age": 35,
        "gender": "Male",
        "phone": "9876543210",
        "disease": "Fever"
    }
]
```

---

### 5. Get Patient by ID

**Method:** `GET`

**Endpoint:**

```text
GET http://127.0.0.1:8000/patients?patient_id=1
```

This returns the patient whose `patient_id` is `1`.

---

### 6. Create a Doctor

**Method:** `POST`

**Endpoint:**

```text
POST http://127.0.0.1:8000/doctors
```

In Postman:

**Body → raw → JSON**

```json
{
    "doctor_id": 1,
    "name": "Dr. Amit Verma",
    "specialization": "Cardiologist",
    "phone": "9988776655"
}
```

**Expected Response:**

```json
{
    "doctor_id": 1,
    "name": "Dr. Amit Verma",
    "specialization": "Cardiologist",
    "phone": "9988776655"
}
```

---

### 7. Get All Doctors

**Method:** `GET`

**Endpoint:**

```text
GET http://127.0.0.1:8000/doctors
```

**Expected Response:**

```json
[
    {
        "doctor_id": 1,
        "name": "Dr. Amit Verma",
        "specialization": "Cardiologist",
        "phone": "9988776655"
    }
]
```

---

## 📋 API Testing Summary

| Feature           | Method | Endpoint                 |
| ----------------- | ------ | ------------------------ |
| Health Check      | GET    | `/health`                |
| Get All Patients  | GET    | `/patients`              |
| Get Patient by ID | GET    | `/patients?patient_id=1` |
| Create Patient    | POST   | `/patients`              |
| Get All Doctors   | GET    | `/doctors`               |
| Create Doctor     | POST   | `/doctors`               |

### Postman Configuration

For POST requests:

1. Open **Postman**
2. Select `POST`
3. Enter the API endpoint
4. Go to **Body**
5. Select **raw**
6. Select **JSON**
7. Enter the request JSON
8. Click **Send**
9. Verify the response and HTTP status code

### HTTP Status Codes

| Status Code | Meaning                             |
| ----------- | ----------------------------------- |
| `200`       | Request successful                  |
| `201`       | Patient/Doctor created successfully |
| `409`       | Patient/Doctor ID already exists    |
| `422`       | Validation error                    |
| `500`       | Server-side error                   |

The API uses **Pydantic validation** to validate patient and doctor input before storing data in SQLite.
