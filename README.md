# Hospital_Management_System
🏥 Hospital Management System (Django + DRF)

A role-based hospital management system built with Django and Django REST Framework (DRF).
This system manages patients, doctors, appointments, and medical records, with authentication and role-based dashboards.

🔹 Features
👥 Authentication & Users

User signup, login, logout (/signup/, /login/, /logout/)

Role-based groups (Doctor / Patient / Admin)

JWT authentication for APIs

👨‍⚕️ Doctors

Doctor dashboard (/doctor_dashboard/)

View assigned patients (/doctor_patient/)

Create medical reports (/create_medical/)

Doctor detail endpoints (/doctor_detail/, /doctor_details/<id>/)

🧑‍🤝‍🧑 Patients

Patient dashboard (/user_dashboard/)

Search doctors by name or specialization (/search/?q=cardiologist)

Book appointments (/book_appointment/)

View appointment list (/appointment_list/)

View assigned doctors (/patient_doctor/)

View medical history (/patient_medical/)

Patient detail endpoints (/patient_detail/, /patient_details/<id>/)

📅 Appointments

Appointment detail endpoints (/appointment_detail/, /appointment_details/<id>/)

📋 Medical Records

Doctor can create medical reports (/create_medical/)

Patients can view their medical records (/patient_medical/)

Medical record endpoints (/medical_record/, /medical_records/<id>/)

🔹 Tech Stack

Backend: Django 5, Django REST Framework

Database: SQLite (default) / PostgreSQL

Auth: Django auth + JWT (via djangorestframework-simplejwt)

API Testing: DRF APIClient, Postman

🔹 Installation
# Clone repository
git clone https://github.com/your-username/hospital_management_system.git
cd hospital_management_system

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

🔹 API Endpoints
🔑 Auth

POST /signup/ → Register user

POST /login/ → Login user (returns JWT)

POST /logout/ → Logout

👨‍⚕️ Doctor

GET /doctor_dashboard/

GET /doctor_patient/

POST /create_medical/

🧑‍🤝‍🧑 Patient

GET /user_dashboard/

POST /book_appointment/

GET /appointment_list/

GET /patient_doctor/

GET /patient_medical/

🔍 Search

GET /search/?q=<name|specialization>

🔹 Example Search API
GET /api/search/?q=cardiologist


Response:

[
  {
    "id": 1,
    "name": "Dr. John Smith",
    "specialization": "Cardiologist",
    "experience_years": 12,
    "phone": "9876543210"
  }
]

🔹 Future Enhancements

Add frontend (React / Vue)

Appointment reminders via email

Role-based dashboards in UI

Billing and pharmacy module

🔹 Screenshots (Optional)

Add screenshots of your Postman tests or Django Admin here.

🔹 License

This project is open-source under the MIT License
