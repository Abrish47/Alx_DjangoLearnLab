# Advanced API Project - Views Documentation

## Overview
The project uses DRF generic views to handle CRUD for the `Book` model, enhanced with filtering, searching, and ordering in `BookListView`.

## Views Configuration

### BookListView
- **Endpoint**: `GET /api/books/`
- **Purpose**: Lists all books with advanced query capabilities.
- **Permissions**: `IsAuthenticatedOrReadOnly`

#### Filtering
- **Implementation**: Uses `DjangoFilterBackend` with `filterset_fields = ['title', 'author__name', 'publication_year']`.
- **Example**: 
  - `GET /api/books/?title=Harry%20Potter` - Filter by exact title.
  - `GET /api/books/?author__name=Rowling` - Filter by author name.
  - `GET /api/books/?publication_year=1997` - Filter by year.

#### Searching
- **Implementation**: Uses `SearchFilter` with `search_fields = ['title', 'author__name']`.
- **Example**: 
  - `GET /api/books/?search=Harry` - Search titles and author names for “Harry”.
  - `GET /api/books/?search=Rowling` - Search for “Rowling” in titles or authors.

#### Ordering
- **Implementation**: Uses `OrderingFilter` with `ordering_fields = ['title', 'publication_year']` and default `ordering = ['title']`.
- **Example**: 
  - `GET /api/books/?ordering=publication_year` - Sort by year (ascending).
  - `GET /api/books/?ordering=-title` - Sort by title (descending).

### Other Views
- **BookDetailView**: `GET /api/books/<int:pk>/`
- **BookCreateView**: `POST /api/books/create/`
- **BookUpdateView**: `PUT /api/books/update/<int:pk>/`
- **BookDeleteView**: `DELETE /api/books/delete/<int:pk>/`

## Usage Examples
- Filter and sort: `GET /api/books/?author__name=Rowling&ordering=-publication_year`
- Search and filter: `GET /api/books/?search=Harry&publication_year=1997`

## Testing Instructions
- Use Postman or curl with query params to test filtering, searching, and ordering.
- Verify results match expected criteria (e.g., correct books returned, proper order).
