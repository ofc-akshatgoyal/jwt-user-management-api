JWT-Based User Management API (Django REST Framework)
A secure backend REST API built using Django REST Framework with JWT authentication, allowing users to sign up, log in, and manage their own data (Notes) through protected CRUD endpoints. This project demonstrates authentication, authorization, ownership-based access control, and proper REST API design.

Features :
1. User can Signup 
2. User Login with JWT tokens
3. JWT - based Authentication 
4. CRUD API'S for user to safely generate, update, delete his notes 
5. Ownership-based Authorization (users can only access their own data)
6. Token expiration handling
7. Clean REST API architecture

Tech Stack:
-> Backend: Django, Django REST Framework
-> Authentication: JWT (djangorestframework-simplejwt)
-> Database: SQLite (development)
-> API Testing: Postman

Authentication Flow: 
1. User signs up
2. User logs in with username & password
3. Backend returns JWT access + refresh tokens
4. Client sends access token in Authorization header
5. Backend validates token and identifies user
6. User can access only their own resources 
   Authorization: Bearer <ACCESS_TOKEN>
7. Then start making or editing notes

Notes Endpoints (JWT Protected):

| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| POST   | `/api/notes/`      | Create a new note           |
| GET    | `/api/notes/`      | List logged-in user's notes |
| PUT    | `/api/notes/<id>/` | Update user's note          |
| DELETE | `/api/notes/<id>/` | Delete user's note          |

Example:
    so we will create a Note here-

    POST /api/notes/
    Authorization: Bearer <ACCESS_TOKEN>

    {
    "title": "JWT Project",
    "content": "Auth + CRUD implemented successfully"
    }

    we will get     
    {
    "id": 1,
    "title": "JWT Project",
    "content": "Auth + CRUD implemented successfully",
    "owner": "username"
    }

Security Highlights:
-> Passwords are hashed using Django’s built-in authentication system
-> JWT tokens are validated on every request
-> Ownership enforced at the database query level
-> No client-side control over resource ownership
-> Unauthorized access returns proper HTTP errors

Structure of the project:
jwt_project/
│
├── accounts/        # Signup & Login logic
│
├── core/            # Notes CRUD APIs
│
├── jwt_project/     # Project settings
│
├── manage.py
└── db.sqlite3


For u:
    How to run this:
        git clone <repo-url>
        cd jwt_project
        python -m venv venv
        venv\Scripts\activate   # Windows
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py runserver
        then open postman and start working on that

Author:
    Akshat Goyal
    Backend Developer | Django REST Framework | JWT Auth
    Machine Learning Engineer (in learning by making prjects phase)

THANK YOU 