# Advanced API Project - Views Documentation

This document outlines the configuration and operation of the generic views in the `api` app of the `advanced_api_project`.

## Overview
The project uses DRF generic views to handle CRUD operations for the `Book` model, with customizations and permissions to meet specific requirements.

## Views Configuration

### BookListView
- **Endpoint**: `GET /api/books/`
- **Purpose**: Lists all books in the database.
- **Permissions**: `IsAuthenticatedOrReadOnly` - Anyone can view, but modifications require authentication.
- **Custom Behavior**: Supports filtering by author name via query parameter (e.g., `?author=Rowling`).

### BookDetailView
- **Endpoint**: `GET /api/books/<int:pk>/`
- **Purpose**: Retrieves details of a single book by ID.
- **Permissions**: `IsAuthenticatedOrReadOnly` - Read-only for unauthenticated users.

### BookCreateView
- **Endpoint**: `POST /api/books/create/`
- **Purpose**: Creates a new book instance.
- **Permissions**: `IsAuthenticated` - Only logged-in users can create.
- **Custom Behavior**: Logs the creation event (prints to console).

### BookUpdateView
- **Endpoint**: `PUT /api/books/<int:pk>/update/`
- **Purpose**: Updates an existing book by ID.
- **Permissions**: `IsAuthenticated` - Only logged-in users can update.
- **Custom Behavior**: Prevents updating `publication_year` to a future year (beyond 2025).

### BookDeleteView
- **Endpoint**: `DELETE /api/books/<int:pk>/delete/`
- **Purpose**: Deletes a book by ID.
- **Permissions**: `IsAuthenticated` - Only logged-in users can delete.

## Custom Settings and Hooks
- **Filtering**: `get_queryset` in `BookListView` adds author name filtering.
- **Validation**: `perform_update` in `BookUpdateView` checks `publication_year`.
- **Logging**: `perform_create` in `BookCreateView` demonstrates custom action on save.

## Testing Instructions
- Use Postman or curl to test endpoints.
- Ensure authentication (e.g., via admin login) for POST, PUT, DELETE.
- Verify read-only access for GET requests without login.
