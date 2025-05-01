# 🎓 Django Learning Management System (LMS)

A full-featured **Learning Management System** built with Django Rest Framework (DRF), supporting **Admin**, **Teacher**, and **Student** roles with JWT authentication and Swagger documentation.

---

## 🚀 Features

### 👨‍🎓 Roles
- **Admin**
  - Create/manage users (students, teachers)
  - Manage course categories
  - View platform statistics
  - Moderate or remove courses

- **Teacher**
  - Create/edit/delete their own courses
  - Upload lessons & materials (videos, PDFs, etc.)
  - Track student progress and provide feedback

- **Student**
  - Browse and enroll in courses
  - View lessons and materials
  - Track course progress
  - Ask questions related to lessons
  - Get certificate on course completion

---

## ⚙️ Tech Stack

- Python 3.x
- Django 4.x
- Django Rest Framework
- Simple JWT (JSON Web Tokens)
- drf-yasg (Swagger Documentation)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/yourusername/lms-backend.git
cd lms-backend
Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


## 📘 API Documentation

You can explore the API using the following documentation UIs:

🔹 [Swagger UI](http://localhost:8000/swagger/)  
A user-friendly interface to test all API endpoints interactively.

🔹 [ReDoc UI](http://localhost:8000/redoc/)  
Clean, readable, and responsive API documentation.

🔹 [Swagger JSON Schema](http://localhost:8000/swagger.json)  
The raw OpenAPI schema in JSON format.
