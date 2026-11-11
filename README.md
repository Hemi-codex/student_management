# Student Management System (Django)

A beginner-friendly CRUD project using Django and SQLite.

## 1. Setup

Open a terminal in this folder and run:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install Django:

```bash
pip install -r requirements.txt
```

## 2. Create the database

```bash
python manage.py makemigrations students
python manage.py migrate
```

## 3. Run the website

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Features

- Add students
- View student list and details
- Update student details
- Delete students
- Search students by name, email, or department

No admin account is required to use the website. To use Django admin, run
`python manage.py createsuperuser` and visit `/admin/`.
