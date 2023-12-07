# User Auth API Documentation

## Overview

The Auth APIs manage operations related to creating user accounts for the platform. The endpoints perform the following operations:
* User registration
* Login
* Logout
* Delete account

## Index

- [Endpoints](#endpoints)
    - [Register User](#1-register-user)
    - [User Login](#2-user-login)
    - [User Logout](#3-user-logout)

### Base URL: `/accounts`

---

### Models

### <a name="the-user-object"></a>The User Object

| Field            | Type    | Description                                  |
|------------------|---------|----------------------------------------------|
| `id`             | int    | Unique identifier of the user.            |
| `first_name` | str | User's first name |
| `last_name` | str | User's last name |
| `username` | varchar | User's unique username |
| `email` | varchar | User's unique email identifier |
| `password1` | varchar | User's password |
| `password2` | varchar | Confirmation password for password1 


---

## <a name="endpoints"></a>Endpoints:


### <a name="register-user"></a>**1. Register User**

- **Endpoint**: `/signup/`
- **HTTP Method**: `POST`
- **Description**: Creates an account for the user with the credentials provided.

| Parameter | Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| first_name | str | User's first name | Yes |
| last_name | str | User's last name | Yes|
| username  | string  | Unique identifier of the user | Yes |
| email | email | Unique email identifier of the user | Yes |
| password1 | varchar | User's strong password | Yes|
| password2 | varchar | Confirmation password for password1 | Yes |

**Request Body**:

```json
{
    "first_name":"John",
    "last_name":"Doe",
    "username": "johnny",
    "email": "johndoe@gmail.com",
    "password1":  "MYpass$$",
    "password2":  "MYpass$$"
}
```

**Responses**:

- `201 Created`: Successfully created an account for the user. Returns access and refresh tokens.

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxOTY0NTAwLCJpYXQiOjE3MDE5NjQyMDAsImp0aSI6IjZhYjE4MTM2ZTc1MzQyNmZiMGMwYzZhMzZiMWYzYWYwIiwidXNlcl9pZCI6NH0.NVEOzKTNq8HY2O_vyHJG53mGUhMXJTJJgV0R5eTkzu4",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwMjA1MDYwMCwiaWF0IjoxNzAxOTY0MjAwLCJqdGkiOiIwZjAxM2ExYjdhMTg0ZTBiOTNlZTRkOWJmMzA2NGEyMSIsInVzZXJfaWQiOjR9.Uc3LMDZNDGzlyiLU8RU0zTbHkcNxeyFQXa3l2rtXLDQ",
    "message": "User successfully registered"
}
```
- `400 Bad Request`: Invalid input or malformed request.
- `500 Internal Server Error`: Unexpected server error.

---

### <a name="user-login"></a>**2. User Login**

- **Endpoint**: `/login/`
- **HTTP Method**: `POST`
- **Description**: Logs a user into their account after verifying their credentials

| Parameter | Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| username  | varchar  | User's unique registered username | Yes |
| password | varchar | User's registered password | Yes|


**Request Body**:

```json
{
    "username": "johnny",
    "password":  "MYpass$$"
}
```

**Responses**:

- `201 Created`: Successfully logs the user into the app and returns token key.
```json
{
    "key": "9c85609b957a0031ef062d8e1b2399bc7cf98ff5"
}
```
- `400 Bad Request`: Invalid input or malformed request.
- `500 Internal Server Error`: Unexpected server error.
---