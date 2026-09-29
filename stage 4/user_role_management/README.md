# User and Role Management API

This project implements user and role management APIs with Django function-based views and `JsonResponse`. It does not use Django REST Framework.

## Setup

```powershell
python -m venv user_role_venv
.\user_role_venv\Scripts\Activate.ps1
python -m pip install django
python manage.py migrate
python manage.py runserver
```

The API is available at `http://127.0.0.1:8000/`.

## Endpoints

### Roles

- `GET /roles/` lists roles. Use `?search=admin` to search by role name.
- `POST /roles/` creates a role with `roleName`, optional `accessModules`, and optional `active`.
- `GET /roles/<role_id>/` retrieves a role.
- `PUT /roles/<role_id>/` updates a role.
- `DELETE /roles/<role_id>/` deletes a role.
- `POST /roles/<role_id>/modules/add/` adds a module using `{"module": "reports"}`.
- `POST /roles/<role_id>/modules/remove/` removes a module using `{"module": "reports"}`.

### Users

- `GET /users/` lists users. Use `?search=alex` to search by first name, last name, or email.
- `POST /users/` creates a user with `firstName`, `lastName`, `email`, `password`, and a role ID in `role`.
- `GET /users/<user_id>/` retrieves a user.
- `PUT /users/<user_id>/` updates a user.
- `DELETE /users/<user_id>/` deletes a user.
- `POST /users/signup/` creates a user with the default role named `User`.
- `POST /users/login/` authenticates by email and password and creates a Django session.
- `POST /users/<user_id>/modules/check/` checks access using `{"module": "reports"}`.
- `PUT /users/bulk-update/` updates selected users. The request must include `userIds` and may include `role`, `firstName`, `lastName`, `email`, `password`, or `is_active`.

## Validation

Run the project checks and tests with:

```powershell
python manage.py check
python manage.py test
```

SQLite is used by default and the development database is created by `python manage.py migrate`.