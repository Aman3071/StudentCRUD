# 🎓 StudentCRUD

A simple **Student Management CRUD Application** built with Python for managing student records.

This project demonstrates the implementation of basic **CRUD operations — Create, Read, Update, and Delete** — for student data.

## 📌 About the Project

StudentCRUD is a backend application designed to manage student information efficiently.

The application allows users to:

- ➕ Add new students
- 📋 View student records
- ✏️ Update existing student information
- 🗑️ Delete student records
- 🔍 Manage student data through CRUD operations

## 🛠️ Tech Stack

- **Python**
- **Django**
- **SQLite**
- **HTML5**
- **CSS3**
- **Git & GitHub**

## ✨ Features

### Create

Add new student records with relevant student information.

### Read

View the list of all registered students.

### Update

Modify existing student details whenever required.

### Delete

Remove student records from the database.

## 📂 Project Structure

```text
StudentCRUD/
│
├── manage.py
├── db.sqlite3
│
├── student/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
└── static/
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aman3071/StudentCRUD.git
```

### 2. Navigate to the Project

```bash
cd StudentCRUD
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database

The project uses **SQLite** as the database.

Student information is stored and managed using Django's ORM.

## 📚 What I Learned

Through this project, I practiced:

- Python fundamentals
- Django project structure
- Django models and ORM
- CRUD operations
- URL routing
- Views and templates
- Database integration
- Git & GitHub workflow

## 🔮 Future Improvements

- Student search and filtering
- Pagination
- Authentication and authorization
- REST API using Django REST Framework
- Improved responsive UI
- PostgreSQL database integration

## 👨‍💻 Author

**Aman Tinmekar**

Python Full Stack Developer

- GitHub: https://github.com/Aman3071

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
