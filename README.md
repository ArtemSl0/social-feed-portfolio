## Social Feed — Custom Portfolio Project

A Django-based social media feed application (Instagram/Reddit-style), 
built as a custom portfolio project following the same architecture 
principles as the Taxi Service project (MVT, CBV, auth, forms, search, tests).

### Core features

- **Custom User model** (`AbstractUser`) with `bio` and `avatar` fields
- **Posts** with text content and multiple images per post
- **Comments** on posts, with custom length validation (max 280 characters)
- **Likes / Dislikes** — single-reaction toggle system (one reaction per 
  user per post, switching between like/dislike, or removing the reaction entirely)
- **Reposts** — toggle system to repost/un-repost another user's post
- **User registration** with email and bio fields, built on top of 
  Django's built-in `UserCreationForm`
- **Login / Logout** via Django's built-in authentication views
- **Edit / Delete** for your own posts only (ownership-restricted via `get_queryset`)
- **User profile page** — shows all posts and reposts made by a user
- **"(edited)" label** on posts that were updated after creation
- **Search** across post content and author username in a single query field
- **Pagination** on the feed (5 posts per page)
- **Multiple image upload** with server-side validation (Pillow) to ensure 
  only real images are accepted
- **Modal image preview** — click any post image to view it enlarged
- **Custom dark purple theme** built with Bootstrap 5 + custom CSS

### Models

- `User` (extends `AbstractUser`)
- `Post`
- `PostImage`
- `Comment`
- `Like` (with a `reaction` field: like/dislike)
- `Repost`

### Tech stack

Django, Bootstrap 5, django-crispy-forms, Pillow, SQLite

### Tests

Covers model string representations, the like/dislike toggle logic 
(including state switching), repost toggling, and access control for 
unauthenticated users.

Link to Website
https://olimp-social-feed.onrender.com