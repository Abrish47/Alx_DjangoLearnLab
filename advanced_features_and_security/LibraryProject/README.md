# Permissions and Groups Setup

## Overview
This Django application (`LibraryProject/bookshelf`) implements custom permissions and groups to control access to `Book` model actions.

## Permissions
Defined in `bookshelf/models.py` for the `Book` model:
- `can_view`: View book list
- `can_create`: Create new books
- `can_edit`: Edit existing books
- `can_delete`: Delete books

## Groups
Configured via Django admin:
1. **Viewers**: Has `bookshelf.can_view`
2. **Editors**: Has `bookshelf.can_create`, `bookshelf.can_edit`
3. **Admins**: Has all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Usage
- Views in `bookshelf/views.py` use `@permission_required` to enforce these permissions.
- Example: `@permission_required('bookshelf.can_edit', raise_exception=True)` restricts `edit_book` to users with `can_edit`.

## Testing
- Create users and assign to groups via admin or shell.
- Test access at `/bookshelf/books/`, `/bookshelf/books/create/`, etc.
