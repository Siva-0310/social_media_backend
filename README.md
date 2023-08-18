# FastAPI social_media_backend App

This project is a simple social_media_backend application built using FastAPI, PostgreSQL, and JWT authentication. It allows users to authenticate, create new posts, and update their own posts.This project demonstrates user authentication and CRUD operations for posts using FastAPI and PostgreSQL.

## Features

- User registration and authentication using JWT tokens.
- Creating new blog posts with a title and content.
- Updating the content of existing posts.

## Installation

1. Clone the repository:

   ```bash
   https://github.com/Siva-0310/social_media_backend.git
   cd social_media_backend
# FastAPI social_media_backend App API Endpoints


### Authentication

#### Login User

Authenticate a user and get a token.

- **Method:** POST
- **Endpoint:** /login/
- **Request Body:**
  - username: string
  - password: string

#### Users

##### Create User

Register a new user.

- **Method:** POST
- **Endpoint:** /users/
- **Request Body:**
  - user_email: string (Email format)
  - user_password: string (Minimum length of 8 characters)
  - user_name: string

### Posts

#### Get All Posts

Retrieve all posts.

- **Method:** GET
- **Endpoint:** /posts/

#### Create Post

Create a new post.

- **Method:** POST
- **Endpoint:** /posts/
- **Request Body:**
  - post_text: string
  - post_votes: integer (Optional)

#### Get Single Post

Retrieve a single post by post_id.

- **Method:** GET
- **Endpoint:** /posts/{post_id}/

#### Update Post

Update a post by post_id.

- **Method:** PUT
- **Endpoint:** /posts/{post_id}/
- **Request Body:**
  - text: string

#### Delete Post

Delete a post by post_id.

- **Method:** DELETE
- **Endpoint:** /posts/{post_id}/

#### Increase Votes

Increase votes for a post by post_id.

- **Method:** PUT
- **Endpoint:** /posts/votes/{post_id}/
# Project Directory Structure

- app
  - database
    - __init__.py
    - connection.py
    - db.sql
    - posts_operations.py
    - user_operations.py
  - routers
    - __init__.py
    - auth.py
    - users.py
    - posts.py
  - schemas
    - __init__.py
    - schemas.py
  - __init__.py
  - main.py
  - oauth2.py
  - utils.py
