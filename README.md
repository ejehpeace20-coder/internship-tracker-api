# internship-tracker-api
A backend API for tracking internship applications using FastAPI, SQLAlchemy ORM, and SQLite. Includes full CRUD functionality, request/response validation, and OpenAPI documentation.

# Internship Tracker API

A RESTful backend API for tracking internship applications.

## Overview
This project allows users to create, view, update, and delete internship applications. It is designed as a backend service with clear API structure and documentation.

## Features
- Create internship applications
- View all applications
- Update application status
- Delete applications
- Auto-generated API documentation with Swagger

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## API Documentation
After running the server, access Swagger UI at:
http://127.0.0.1:8000/docs

## How to Run Locally
```bash
pip install fastapi sqlalchemy uvicorn
uvicorn app.main:app --reload

