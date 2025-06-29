# FastAPI Intern Assessment - Task Management API

## Overview

This assessment is designed to evaluate your proficiency with modern Python web development using FastAPI, Pydantic, and SQLModel. You will build a task management API that demonstrates your understanding of RESTful APIs, data validation, database operations, and clean code practices.

## Technical Requirements

### Core Technologies

- **FastAPI** - Web framework for building the API
- **Pydantic** - Data validation and serialization
- **SQLModel** - ORM for database operations (built on SQLAlchemy)
- **SQLite** - Database (for simplicity)

### Python Version

- Python 3.9 or higher

## Project Specification

### Database Schema

Create a Task model with the following fields:


| Field       | Type     | Constraints                  | Description            |
| ------------- | ---------- | ------------------------------ | ------------------------ |
| id          | Integer  | Primary Key, Auto-increment  | Unique task identifier |
| title       | String   | Required, Max 200 chars      | Task title             |
| description | String   | Optional, Max 1000 chars     | Task description       |
| status      | Enum     | Required, Default: "pending" | Task status            |
| priority    | Enum     | Required, Default: "medium"  | Task priority          |
| created_at  | DateTime | Auto-generated               | Creation timestamp     |
| updated_at  | DateTime | Optional                     | Last update timestamp  |
| due_date    | DateTime | Optional                     | Task deadline          |
| assigned_to | String   | Optional, Max 100 chars      | Assignee name          |

### Enums

**TaskStatus:**

- pending
- in_progress
- completed
- cancelled

**TaskPriority:**

- low
- medium
- high
- urgent

### API Endpoints

Implement the following RESTful endpoints:

#### 1. Root Endpoint

- **GET /** - Return API information and available endpoints

#### 2. Health Check

- **GET /health** - Return API health status

#### 3. Task Management

- **POST /tasks** - Create a new task
- **GET /tasks** - List all tasks with optional filtering and pagination
- **GET /tasks/{task_id}** - Retrieve a specific task
- **PUT /tasks/{task_id}** - Update an existing task
- **DELETE /tasks/{task_id}** - Delete a task

#### 4. Filtering Endpoints

- **GET /tasks/status/{status}** - Get tasks by status
- **GET /tasks/priority/{priority}** - Get tasks by priority

### Request/Response Models

Create appropriate Pydantic models for:

1. **TaskCreate** - For creating new tasks
2. **TaskUpdate** - For updating existing tasks (all fields optional)
3. **TaskResponse** - For API responses

### Validation Requirements

Implement the following validation rules:

1. **Title validation:**

   - Cannot be empty or whitespace only
   - Must be trimmed of leading/trailing spaces
2. **Due date validation:**

   - Must be in the future (if provided)
3. **Proper HTTP status codes:**

   - 201 for successful creation
   - 200 for successful retrieval/update
   - 404 for not found
   - 422 for validation errors
   - 400 for other client errors

### Features to Implement

1. **CRUD Operations** - Full Create, Read, Update, Delete functionality
2. **Data Validation** - Comprehensive input validation using Pydantic
3. **Error Handling** - Proper error responses with meaningful messages
4. **Pagination** - Support for skip/limit query parameters
5. **Filtering** - Filter tasks by status and priority
6. **Database Integration** - Proper SQLModel/SQLAlchemy integration
7. **API Documentation** - Automatic OpenAPI/Swagger documentation

## Deliverables

### 1. Code Structure

Organize your code with:

- Clear separation of models, API routes, and database logic
- Proper imports and dependencies
- Clean, readable code with appropriate comments

### 2. Documentation

- Include a README.md with setup instructions
- Document any assumptions or design decisions
- Provide example API calls

### 3. Testing Instructions

Include instructions for:

- Installing dependencies
- Running the application
- Accessing the API documentation
- Testing the endpoints

## Evaluation Criteria

You will be evaluated on:

### Technical Implementation (40%)

- Correct use of FastAPI, Pydantic, and SQLModel
- Proper database schema and relationships
- Implementation of all required endpoints
- Code organization and structure

### Data Validation (25%)

- Comprehensive Pydantic models
- Custom validators where appropriate
- Proper error handling and responses
- Input sanitization

### API Design (20%)

- RESTful API principles
- Appropriate HTTP methods and status codes
- Consistent response formats
- Clear endpoint naming

### Code Quality (15%)

- Clean, readable code
- Proper error handling
- Efficient database queries
- Following Python best practices

## Bonus Points

Implement any of the following for extra credit:

1. **Advanced Filtering** - Support for multiple simultaneous filters
2. **Sorting** - Sort tasks by different fields
3. **Search** - Text search in title/description
4. **Bulk Operations** - Update/delete multiple tasks
5. **Database Migrations** - Proper database versioning
6. **Unit Tests** - Basic test coverage
7. **Docker** - Containerized application
8. **Environment Configuration** - Support for different environments

## Submission Requirements

1. **Source Code** (Github Repo) - Complete, runnable Python application
2. **README.md** - Clear setup and usage instructions
3. **requirements.txt** - List of Python dependencies
4. **Sample Data** - Optional: Include sample API calls or test data

### Setup Instructions Template

Your README should include:

```bash
# Installation
pip install -r requirements.txt

# Run the application
python main.py

# Access API documentation
http://localhost:8000/docs

# Example API calls
curl -X POST "http://localhost:8000/tasks" \
     -H "Content-Type: application/json" \
     -d '{"title": "Sample Task", "priority": "high"}'
```

## Timeline

- **Submission Deadline:** Jun 29

## Learning Resources

### Official Documentation

- **FastAPI Documentation:** https://fastapi.tiangolo.com/
  - Tutorial: https://fastapi.tiangolo.com/tutorial/
  - Advanced User Guide: https://fastapi.tiangolo.com/advanced/
- **Pydantic Documentation:** https://docs.pydantic.dev/latest/
  - Models: https://docs.pydantic.dev/latest/concepts/models/
  - Validators: https://docs.pydantic.dev/latest/concepts/validators/
- **SQLModel Documentation:** https://sqlmodel.tiangolo.com/
  - Tutorial: https://sqlmodel.tiangolo.com/tutorial/

### Essential Tutorials

- **FastAPI Full Tutorial:** https://fastapi.tiangolo.com/tutorial/first-steps/
- **SQLModel with FastAPI:** https://sqlmodel.tiangolo.com/tutorial/fastapi/
- **Pydantic Models Guide:** https://docs.pydantic.dev/latest/concepts/models/

### Helpful Articles and Blogs

- **Real Python - FastAPI Tutorial:** https://realpython.com/fastapi-python-web-apis/
- **Building APIs with FastAPI and SQLModel:** https://testdriven.io/blog/fastapi-sqlmodel/
- **FastAPI Best Practices:** https://github.com/zhanymkanov/fastapi-best-practices

### Common Patterns and Examples

- **FastAPI Dependency Injection:** https://fastapi.tiangolo.com/tutorial/dependencies/
- **Error Handling in FastAPI:** https://fastapi.tiangolo.com/tutorial/handling-errors/
- **Database Sessions with SQLModel:** https://sqlmodel.tiangolo.com/tutorial/fastapi/session/
- **Response Models:** https://fastapi.tiangolo.com/tutorial/response-model/

### Sample Project Structure

- **FastAPI Project Structure Guide:** https://github.com/tiangolo/full-stack-fastapi-postgresql
- **Python Project Layout:** https://realpython.com/python-application-layouts/

### Testing Your API

Once your server is running, visit:

- **Interactive Documentation:** http://localhost:8000/docs
- **Alternative Documentation:** http://localhost:8000/redoc
- **OpenAPI Schema:** http://localhost:8000/openapi.json

## Questions?

If you have any questions about the requirements or need clarification on any aspect of the assignment, please don't hesitate to ask. The resources above should help you get started and overcome common challenges.

Good luck, and we look forward to reviewing your implementation!
