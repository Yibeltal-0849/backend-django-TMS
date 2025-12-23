# Task Management System - Backend API

A Django REST Framework based Task Management System API.

## Features
- User authentication with JWT tokens
- Project management
- Task management with comments
- User profiles
- File attachments
- Role-based permissions

## Installation

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and configure
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`

## API Documentation

- API Root: `http://localhost:8000/api/`
- Admin Panel: `http://localhost:8000/admin/`
- API Schema: `http://localhost:8000/api/schema/`

## Endpoints

### Authentication
- POST `/api/users/login/` - Login with JWT tokens
- POST `/api/users/register/` - Register new user
- POST `/api/users/token/refresh/` - Refresh JWT token

### Projects
- GET `/api/projects/` - List all projects
- POST `/api/projects/` - Create new project
- GET `/api/projects/{id}/` - Get project details
- PUT/PATCH `/api/projects/{id}/` - Update project
- DELETE `/api/projects/{id}/` - Delete project

### Tasks
- GET `/api/tasks/` - List all tasks
- POST `/api/tasks/` - Create new task
- GET `/api/tasks/{id}/` - Get task details
- PUT/PATCH `/api/tasks/{id}/` - Update task
- DELETE `/api/tasks/{id}/` - Delete task

## Environment Variables
See `.env.example` for all available environment variables.