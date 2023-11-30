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


---

## <a name="endpoints"></a>Endpoints:


### <a name="register-user"></a>**1. Register User**

- **Endpoint**: `/signup/`
- **HTTP Method**: `POST`
- **Description**: Creates an account for the user with the credentials provided.

| Parameter | Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| username  | string  | Unique identifier of the user | Yes |
| email | email | Unique email identifier of the user | Yes |
| password1 | varchar | User's strong password | Yes|
| password2 | varchar | Confirmation password for password1 | Yes | 

**Request Body**:

```json
{
    "username": "johnny",
    "email": "johndoe@gmail.com",
    "password1":  "MYpass$$",
    "password2":  "MYpass$$"
}
```

**Responses**:

- `201 Created`: Successfully created an account for the user.
- `400 Bad Request`: Invalid input or malformed request.
- `500 Internal Server Error`: Unexpected server error.

---

### <a name="user-login"></a>**2. User Login**

- **Endpoint**: `/login/`
- **HTTP Method**: `POST`
- **Description**: Logs a user into their account after verifying their credentials

| Parameter | Type | Description                      | Required |
|-----------|------|----------------------------------|----------|
| username  | string  | User's unique registered username | Yes |
| email | email | User's registered email | Yes |
| password | varchar | User's registered password | Yes|


**Request Body**:

```json
{
    "username": "johnny",
    "email": "johndoe@gmail.com",
    "password":  "MYpass$$"
}
```

**Responses**:

- `201 Created`: Successfully created an account for the user.
- `400 Bad Request`: Invalid input or malformed request.
- `500 Internal Server Error`: Unexpected server error.

---