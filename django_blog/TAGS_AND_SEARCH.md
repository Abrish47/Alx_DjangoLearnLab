# Django Blog Tagging and Search Documentation

This document details the tagging and search features in the `django_blog` project.

## Overview
- **Tagging**: Users can add tags to posts for categorization.
- **Search**: Users can search posts by title, content, or tags.

## Components
- **Model**: `Post` (`blog/models.py`)
  - Added `tags = TaggableManager()` via `django-taggit`.
- **Form**: `PostForm` (`blog/forms.py`)
  - Updated to include `tags` field.
- **Views**: (`blog/views.py`)
  - `TagListView`: Filters posts by tag.
  - `search`: Searches posts using `Q` objects.
- **URLs**: (`blog/urls.py`)
  - `/tags/<slug:tag>/`: Tag filter.
  - `/search/`: Search results.
- **Templates**:
  - `base.html`: Added search bar.
  - `post_list.html`, `post_detail.html`: Display tags.
  - `search_results.html`: Shows search results.

## Usage
- **Add Tags**: In `/post/new/` or `/post/<pk>/update/`, enter tags (e.g., “python, django”).
- **View Tags**: See tags on post list/detail pages; click to filter.
- **Search**: Use the nav bar search, enter a keyword, see results.

## Testing
- Start: `python manage.py runserver`.
- Tags: Create a post with tags, check `/post/` and `/tags/python/`.
- Search: Search “python” in nav bar, verify results on `/search/`.

## Notes
- Uses `django-taggit` for tagging.
- Search is case-insensitive and matches tags distinctly.