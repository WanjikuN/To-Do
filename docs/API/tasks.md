# Task Management API Documentation

## Overview

The Task Management API provides a complete RESTful interface for managing tasks. It supports creating, reading, updating, and deleting (soft delete) tasks, along with filtering, searching, and pagination capabilities.

**Base URL:** `{{baseUrl}}/api/v1/tasks/`

---

## Endpoints

### 1. List Tasks

Retrieves a paginated list of active (non-archived) tasks with optional filtering and searching.

**Endpoint:** `GET {{baseUrl}}/api/v1/tasks/`

#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number for pagination (default: 1) |
| `status` | string | No | Filter by task status (e.g., `todo`, `in_progress`, `completed`) |
| `priority` | string | No | Filter by priority level (e.g., `low`, `medium`, `high`) |
| `search` | string | No | Search term to match against task title and description |

#### Response Format

**Success Response (200 OK):**

```json
{
  "code": 200,
  "message": "Tasks retrieved successfully",
  "tasks": [
    {
      "id": 1,
      "title": "Complete API documentation",
      "description": "Write comprehensive docs for the task API",
      "status": "todo",
      "priority": "high",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "is_archived": false
    }
  ],
  "count": 25,
  "next": "{{baseUrl}}/api/v1/tasks/?page=2",
  "previous": null
}
```

#### Example Requests

**Example 1: Get all high priority tasks that are in todo status**

```bash
GET {{baseUrl}}/api/v1/tasks/?priority=high&status=todo
```

**Response:**
```json
{
  "code": 200,
  "message": "Tasks retrieved successfully",
  "tasks": [
    {
      "id": 1,
      "title": "Complete API documentation",
      "description": "Write comprehensive docs for the task API",
      "status": "todo",
      "priority": "high",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "is_archived": false
    },
    {
      "id": 5,
      "title": "Review security audit",
      "description": "Check and address security vulnerabilities",
      "status": "todo",
      "priority": "high",
      "created_at": "2024-01-16T14:20:00Z",
      "updated_at": "2024-01-16T14:20:00Z",
      "is_archived": false
    }
  ],
  "count": 2,
  "next": null,
  "previous": null
}
```

**Example 2: Search for tasks containing "documentation" with pagination**

```bash
GET {{baseUrl}}/api/v1/tasks/?search=documentation&page=1
```

**Response:**
```json
{
  "code": 200,
  "message": "Tasks retrieved successfully",
  "tasks": [
    {
      "id": 1,
      "title": "Complete API documentation",
      "description": "Write comprehensive docs for the task API",
      "status": "todo",
      "priority": "high",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z",
      "is_archived": false
    },
    {
      "id": 12,
      "title": "Update user documentation",
      "description": "Refresh user guide with latest features",
      "status": "in_progress",
      "priority": "medium",
      "created_at": "2024-01-14T09:15:00Z",
      "updated_at": "2024-01-15T11:45:00Z",
      "is_archived": false
    }
  ],
  "count": 2,
  "next": null,
  "previous": null
}
```

---

### 2. Retrieve Single Task

Retrieves details for a specific task by ID.

**Endpoint:** `GET {{baseUrl}}/api/v1/tasks/{id}/`

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | Unique identifier of the task |

#### Response Format

**Success Response (200 OK):**

```json
{
  "code": 200,
  "task": {
    "id": 1,
    "title": "Complete API documentation",
    "description": "Write comprehensive docs for the task API",
    "status": "todo",
    "priority": "high",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "is_archived": false
  }
}
```

#### Example Request

```bash
GET {{baseUrl}}/api/v1/tasks/1/
```

**Response:**
```json
{
  "code": 200,
  "task": {
    "id": 1,
    "title": "Complete API documentation",
    "description": "Write comprehensive docs for the task API",
    "status": "todo",
    "priority": "high",
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z",
    "is_archived": false
  }
}
```

---

### 3. Create Task

Creates a new task.

**Endpoint:** `POST {{baseUrl}}/api/v1/tasks/`

#### Request Body

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | Task title |
| `description` | string | No | Detailed task description |
| `status` | string | No | Task status (default: `todo`) |
| `priority` | string | No | Priority level (default: `medium`) |

**Request Example:**

```json
{
  "title": "Implement user authentication",
  "description": "Add JWT-based authentication to the API",
  "status": "todo",
  "priority": "high"
}
```

#### Response Format

**Success Response (201 Created):**

```json
{
  "code": 201,
  "message": "Task successfully created",
  "task": {
    "id": 15,
    "title": "Implement user authentication",
    "status": "todo"
  }
}
```

#### Example Request

```bash
POST {{baseUrl}}/api/v1/tasks/
Content-Type: application/json

{
  "title": "Implement user authentication",
  "description": "Add JWT-based authentication to the API",
  "status": "todo",
  "priority": "high"
}
```

**Response:**
```json
{
  "code": 201,
  "message": "Task successfully created",
  "task": {
    "id": 15,
    "title": "Implement user authentication",
    "status": "todo"
  }
}
```

---

### 4. Update Task (Full Update)

Updates all fields of an existing task.

**Endpoint:** `PUT {{baseUrl}}/api/v1/tasks/{id}/`

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | Unique identifier of the task |

#### Request Body

All fields from the create endpoint should be provided.

**Request Example:**

```json
{
  "title": "Implement user authentication - Updated",
  "description": "Add JWT-based authentication with refresh tokens",
  "status": "in_progress",
  "priority": "high"
}
```

#### Response Format

**Success Response (200 OK):**

```json
{
  "code": 200,
  "message": "Task successfully updated",
  "task": {
    "id": 15,
    "title": "Implement user authentication - Updated",
    "status": "in_progress"
  }
}
```

---

### 5. Partial Update Task

Updates specific fields of an existing task without requiring all fields.

**Endpoint:** `PATCH {{baseUrl}}/api/v1/tasks/{id}/`

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | Unique identifier of the task |

#### Request Body

Any subset of task fields can be provided.

**Request Example:**

```json
{
  "status": "completed"
}
```

#### Response Format

**Success Response (200 OK):**

```json
{
  "code": 200,
  "message": "Task successfully updated",
  "task": {
    "id": 15,
    "title": "Implement user authentication - Updated",
    "status": "completed"
  }
}
```

#### Example Request

```bash
PATCH {{baseUrl}}/api/v1/tasks/15/
Content-Type: application/json

{
  "status": "completed",
  "priority": "medium"
}
```

**Response:**
```json
{
  "code": 200,
  "message": "Task successfully updated",
  "task": {
    "id": 15,
    "title": "Implement user authentication - Updated",
    "status": "completed"
  }
}
```

---

### 6. Delete Task (Soft Delete)

Archives a task instead of permanently deleting it. Archived tasks won't appear in list or retrieve endpoints.

**Endpoint:** `DELETE {{baseUrl}}/api/v1/tasks/{id}/`

#### Path Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | Unique identifier of the task |

#### Response Format

**Success Response (200 OK):**

```json
{
  "code": 200,
  "message": "Task successfully archived",
  "task_id": 15
}
```

#### Example Request

```bash
DELETE {{baseUrl}}/api/v1/tasks/15/
```

**Response:**
```json
{
  "code": 200,
  "message": "Task successfully archived",
  "task_id": 15
}
```

---

## Authentication Requirements

**Authentication:** This API requires authentication for all endpoints. The specific authentication method (API key, JWT, session-based, etc.) should be configured according to your Django REST Framework settings.

**Header Format:**
```
Authorization: Bearer <your-access-token>
```

or

```
Authorization: Token <your-api-key>
```

**Note:** Ensure the authentication credentials are included in all requests. Unauthenticated requests will receive a 401 Unauthorized response.

---

## Error Responses

### Common Error Status Codes

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid input data or malformed request |
| 401 | Unauthorized - Missing or invalid authentication credentials |
| 403 | Forbidden - Authenticated but lacks permission to access resource |
| 404 | Not Found - Task with specified ID doesn't exist or is archived |
| 500 | Internal Server Error - Server-side error occurred |

### Error Response Format

All error responses follow this structure:

```json
{
  "detail": "Error message describing what went wrong"
}
```

or for validation errors:

```json
{
  "field_name": [
    "Error message for this field"
  ]
}
```

### Example Error Responses

**400 Bad Request - Validation Error:**

```json
{
  "title": [
    "This field is required."
  ],
  "priority": [
    "\"urgent\" is not a valid choice."
  ]
}
```

**401 Unauthorized:**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

**404 Not Found:**

```json
{
  "detail": "Not found."
}
```

**404 Task Not Found (specific case):**

When requesting a task that has been archived or doesn't exist:

```bash
GET {{baseUrl}}/api/v1/tasks/999/
```

**Response:**
```json
{
  "detail": "Not found."
}
```

---

## Rate Limiting

**Current Configuration:** Rate limiting should be configured at the server level or through Django REST Framework's throttling classes.

**Recommended Limits:**
- Anonymous users: 100 requests per hour
- Authenticated users: 1000 requests per hour

**Rate Limit Headers:**
When rate limiting is enforced, responses include:
- `X-RateLimit-Limit`: Maximum requests allowed
- `X-RateLimit-Remaining`: Remaining requests in current window
- `X-RateLimit-Reset`: Timestamp when the limit resets

**Rate Limit Exceeded Response (429):**

```json
{
  "detail": "Request was throttled. Expected available in 3600 seconds."
}
```

---

## Special Considerations

### 1. Soft Delete Architecture

- **DELETE operations archive tasks** rather than permanently removing them
- Archived tasks have `is_archived=True` and won't appear in list or retrieve queries
- This preserves data integrity and allows for potential recovery
- To permanently delete tasks, database-level operations are required

### 2. Pagination

- List endpoints return paginated results by default
- Page size is configured in Django REST Framework settings
- Use the `next` and `previous` fields in responses to navigate pages
- The `count` field shows total matching results

### 3. Filtering and Search Behavior

- **Filtering:** Exact matches on `status` and `priority` fields
- **Searching:** Case-insensitive partial matches on `title` and `description`
- Filters and search can be combined in a single request
- All filters apply to non-archived tasks only

### 4. Task Ordering

- Tasks are ordered by `created_at` in descending order (newest first)
- This ordering applies before pagination and filtering

### 5. Field Validation

Expected values for enumerated fields:

**Status values:**
- `todo`
- `in_progress`
- `completed`

**Priority values:**
- `low`
- `medium`
- `high`

(Actual valid values depend on your Task model choices)

### 6. Request/Response Content Type

- All requests should use `Content-Type: application/json`
- All responses return `Content-Type: application/json`

### 7. CORS Considerations

If accessing this API from a web browser, ensure CORS (Cross-Origin Resource Sharing) is properly configured on the server.

---

## Complete Example Workflow

### Workflow: Create, Update, and Archive a Task

**Step 1: Create a new task**

```bash
POST {{baseUrl}}/api/v1/tasks/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Fix login bug",
  "description": "Users unable to login with special characters in password",
  "status": "todo",
  "priority": "high"
}
```

**Response:**
```json
{
  "code": 201,
  "message": "Task successfully created",
  "task": {
    "id": 42,
    "title": "Fix login bug",
    "status": "todo"
  }
}
```

**Step 2: Update task status to in_progress**

```bash
PATCH {{baseUrl}}/api/v1/tasks/42/
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "in_progress"
}
```

**Response:**
```json
{
  "code": 200,
  "message": "Task successfully updated",
  "task": {
    "id": 42,
    "title": "Fix login bug",
    "status": "in_progress"
  }
}
```

**Step 3: Mark task as completed**

```bash
PATCH {{baseUrl}}/api/v1/tasks/42/
Authorization: Bearer <token>
Content-Type: application/json

{
  "status": "completed"
}
```

**Response:**
```json
{
  "code": 200,
  "message": "Task successfully updated",
  "task": {
    "id": 42,
    "title": "Fix login bug",
    "status": "completed"
  }
}
```

**Step 4: Archive the completed task**

```bash
DELETE {{baseUrl}}/api/v1/tasks/42/
Authorization: Bearer <token>
```

**Response:**
```json
{
  "code": 200,
  "message": "Task successfully archived",
  "task_id": 42
}
```

---

## Support and Contact

For additional support or questions about this API, please contact your API administrator or refer to the main API documentation portal.

**API Version:** v1  
**Last Updated:** February 2026