# Task Management App

A **personal task management application** built with **Django REST Framework (DRF)** and a React frontend.  
This app allows you to create, update, delete (soft delete), and view tasks with priorities, statuses, and tags.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
  - [List Tasks](#list-tasks)
  - [Retrieve Task](#retrieve-task)
  - [Create Task](#create-task)
  - [Update Task](#update-task)
  - [Delete (Archive) Task](#delete-archive-task)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **CRUD operations** for tasks
- **Soft delete** via `is_archived` flag
- **Filter & search** tasks by status, priority, title, or description
- **Custom API responses** for all endpoints (consistent JSON messages)
- **Task metadata**: priority, status, due date, tags, created/updated timestamps

---

## Tech Stack

- **Backend**: Django 5.x, Django REST Framework
- **Database**: PostgreSQL (or SQLite for development)
- **Frontend**: React (optional for this personal project)
- **Environment Management**: Python `venv`, `django-environ`

---

## Getting Started

### Requirements

- Python 3.10+
- pip
- Node.js + npm/yarn (if using React frontend)
- PostgreSQL (optional, can use SQLite for local dev)

---

### Installation

1. **Clone the repository:**

   ```Bash
   git clone [https://github.com/yourusername/task-app.git](https://github.com/yourusername/task-app.git)
   cd task-app
   ```

2. **Create and activate a virtual environment:**

   ```Bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies:**

   ```Bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables (example .env):**

   ```python
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=
   ```

5. **Run migrations:**

   ```Bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional, for admin panel):**
   ```Bash
   python manage.py createsuperuser
   ```

---

## Running the Project

```Bash
python manage.py runserver 0.0.0.0:8081
```

Access API via: http://localhost:8081/api/tasks/

Access admin panel via: http://localhost:8081/admin/

## API Endpoints

All responses are JSON with a consistent format:

```JSON
{
"code": 200,
"message": "Success message",
"task": { ... }
}
```

### List Tasks

- URL: `/api/tasks/`

- Method: GET

- Description: Retrieves all non-archived tasks. Supports filtering and search.

- Query Parameters:

  - status: todo, in_progress, done

  - priority: low, medium, high

  - search: search in title/description

Example Response:

```JSON
{
"code": 200,
"message": "Tasks retrieved successfully",
"tasks": [
{
"id": 1,
"title": "Finish tasks app UI",
"status": "todo"
}
]
}
```

### Retrieve Task

- URL: /api/tasks/{id}/

- Method: GET

- Description: Retrieve details of a single task.

### Create Task

- URL: /api/tasks/

- Method: POST

Body:

```JSON
{
"title": "Transfer Process",
"description": "Admin Parcel Applications",
"status": "todo",
"priority": "medium",
"due_date": "2026-02-06",
"tags": ["count", "get", "permissions"]
}
```

### Update Task

- URL: /api/tasks/{id}/

- Method: PUT (full update) or PATCH (partial update)

### Delete (Archive) Task

- URL: /api/tasks/{id}/

- Method: DELETE

- Behavior: Soft delete — sets is_archived = true

## Contributing

  1. Fork the repo.

  2. Create a branch:`git checkout -b feature/your-feature`.

  3. Commit your changes: `git commit -m "Add feature"`.

  4. Push: `git push origin feature/your-feature`.

  5. Open a pull request.

## License

This project is MIT Licensed.

