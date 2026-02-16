# Capstone Project – Real-Time Collaborative Project Management Tool

## Overview

This capstone project is a hybrid monolith/microservice application designed to simulate a production-grade backend architecture.

The system consists of:

- A Django REST API (monolithic core)
- A Node.js WebSocket microservice (real-time notifications)

## Architecture

### Monolith (Django + DRF)
- User authentication
- Project management
- Task management
- Commenting system
- PostgreSQL database

### Microservice (Node.js)
- Real-time updates
- WebSocket broadcasting
- Event-driven architecture

## Tech Stack

- Python 3.10
- Django
- Django REST Framework
- Node.js
- PostgreSQL
- Poetry
- Docker (coming soon)
- GitHub Actions (CI/CD – coming soon)

## Setup (Development)

```bash
poetry install
poetry run python --version

