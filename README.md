# Capstone Project -- Secure Real-Time Project Management API

![Python](https://img.shields.io/badge/python-3.12-blue)
![Django](https://img.shields.io/badge/django-5.x-green)
![DRF](https://img.shields.io/badge/django--rest--framework-3.x-red)
![JWT](https://img.shields.io/badge/authentication-JWT-orange)
![CodeStyle](https://img.shields.io/badge/code%20style-black-000000)

------------------------------------------------------------------------

## Overview

This capstone project simulates a production-grade backend system for a
collaborative project management platform.

The system follows a modular monolith architecture with clean separation
of domains and integrates secure JWT authentication, object-level
permissions, and OpenAPI documentation.

------------------------------------------------------------------------

## Architecture

### Backend (Django + DRF)

-   Secure REST API
-   JWT Authentication (SimpleJWT)
-   Object-level permissions
-   PostgreSQL database
-   ViewSets & Routers (Convention over Configuration)

### Real-Time Layer (Node.js -- Planned Extension)

-   WebSocket notifications
-   Event broadcasting
-   Microservice-ready structure

------------------------------------------------------------------------

## System Design (Logical Flow)

Client (Browser / Mobile / API Client) ↓ JWT Authentication Layer ↓ DRF
ViewSets ↓ Permission Layer (IsAuthenticated + IsOwnerOrReadOnly) ↓
Business Logic (Slug generation, Ownership enforcement) ↓ Django ORM ↓
PostgreSQL

------------------------------------------------------------------------

## Security Model

### Authentication

-   Stateless JWT (access + refresh tokens)
-   Short-lived access tokens
-   Refresh rotation enabled
-   Token blacklisting supported

### Authorization

-   Global `IsAuthenticated`
-   Custom `IsOwnerOrReadOnly`
-   Server-side ownership assignment
-   No client ownership spoofing allowed

------------------------------------------------------------------------

##  Local Development Setup

### Prerequisites

- Python 3.12+
- Poetry
- Docker (installed and running)

### 1. Clone Repository

    git clone https://github.com/yash-solanki09442/capstone-project.git
    cd capstone-project

### 2. Start PostgreSQL via Docker

    docker compose up -d
    docker ps

### 3. Install Dependencies

    poetry install

### 4. Run Migrations

    poetry run python manage.py migrate

### 5. Create Superuser

    poetry run python manage.py createsuperuser

### 6. Start Server

    poetry run python manage.py runserver

API Base URL:

    http://127.0.0.1:8000/api/

Database Configuration

    DB_NAME=capstone
    DB_USER=capstone
    DB_PASSWORD=capstone
    DB_HOST=localhost
    DB_PORT=5432

------------------------------------------------------------------------

## JWT Authentication Flow

### Obtain Token

    curl -X POST http://127.0.0.1:8000/api/auth/token/   -H "Content-Type: application/json"   -d '{"username":"your_username","password":"your_password"}'

Response:

    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }

### Call Protected Endpoint

    curl http://127.0.0.1:8000/api/projects/   -H "Authorization: Bearer <access_token>"

------------------------------------------------------------------------

## API Documentation

Swagger UI:

    http://127.0.0.1:8000/api/docs/

OpenAPI Schema:

    http://127.0.0.1:8000/api/schema/

Generate schema file:

    poetry run python manage.py spectacular --file openapi.yaml

------------------------------------------------------------------------

## Core API Endpoints

### Projects

-   GET /api/projects/
-   POST /api/projects/
-   GET /api/projects/{id}/
-   PATCH /api/projects/{id}/
-   DELETE /api/projects/{id}/

### Tasks

-   GET /api/tasks/
-   POST /api/tasks/
-   GET /api/tasks/{id}/
-   PATCH /api/tasks/{id}/
-   DELETE /api/tasks/{id}/

### Comments

-   GET /api/comments/
-   POST /api/comments/
-   GET /api/comments/{id}/
-   PATCH /api/comments/{id}/
-   DELETE /api/comments/{id}/

------------------------------------------------------------------------

## Example Response (Create Project)

    {
      "id": 1,
      "title": "API Security Project",
      "slug": "api-security-project",
      "description": "Example project",
      "owner": 1,
      "created_at": "2026-02-24T08:10:21Z",
      "updated_at": "2026-02-24T08:10:21Z"
    }

------------------------------------------------------------------------

## Code Quality

Pre-commit hooks configured: - Black (formatting) - isort (import
sorting) - flake8 (linting)

Run manually:

    poetry run pre-commit run --all-files

------------------------------------------------------------------------

## Milestone Status

✔ Milestone 1 -- Data Models & Admin\
✔ Milestone 2 -- Secure JWT REST API & Documentation

------------------------------------------------------------------------

## Roadmap

-   Filtering & Pagination
-   Query Optimization
-   Rate Limiting
-   GitHub Actions CI/CD
-   Dockerization
-   Cloud Deployment

------------------------------------------------------------------------

## Author

Yash Solanki\
Senior Software Engineer -- Python \| Django \| DRF

------------------------------------------------------------------------