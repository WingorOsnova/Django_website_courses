Courses Shop (Django)

Admin name: guest
password: g123456g

Overview
- A simple courses catalog/shop built with Django and Bootstrap.
- Exposes a REST-like API using django-tastypie.
- Public read access for API; write actions require API key.
- Admin interface customized with inline editing and optional django-jet theme.

Key Features
- Data model: `Category` and `Course` (with `ForeignKey` from Course to Category).
- Web UI: list all courses and view a single course detail.
- Admin: list displays, inline courses under categories, basic branding.
- API: `GET` open to everyone; `POST/PUT/DELETE` protected by API key.
- API hydrate/dehydrate to work with `category_id` cleanly.

Tech Stack
- Python 3.10+
- Django 4.0.8
- django-tastypie 0.15.1
- Bootstrap 5.3 (via CDN)
- SQLite (default)
- Optional: django-jet (admin UI theme)

Project Structure
- `base/` – settings, URLs, WSGI/ASGI.
- `shop/` – domain app: models, views, urls, admin, migrations.
- `api/` – tastypie resources, authentication, urls.
- `templates/` – base layout and shop templates.
- `manage.py`, `requirements.txt`, `db.sqlite3`.

Running Locally
1) Create and activate a virtualenv
   - `python -m venv .venv`
   - macOS/Linux: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`

2) Install dependencies
   - `pip install -r requirements.txt`
   - Optional (admin theme): `pip install django-jet`

3) Apply migrations
   - `python manage.py migrate`

4) Create a superuser (to access admin and generate API keys)
   - `python manage.py createsuperuser`

5) Run the dev server
   - `python manage.py runserver`
   - Web UI: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
   - API root: http://127.0.0.1:8000/api/v1/

Web UI
- Courses list: `/` (click a title to open details)
- Course details: `/<course_id>`

Admin
- Custom titles and inline editing of Courses inside Categories.
- If you don’t install `django-jet`, remove `jet` and `jet.dashboard` from `INSTALLED_APPS` in `base/settings.py` or install the package.

API (Tastypie)
- Root: `/api/v1/`
- Resources:
  - `GET /api/v1/categories/`
  - `GET /api/v1/courses/`
  - `POST /api/v1/courses/` (requires API key)
  - `PUT /api/v1/courses/<id>/` (requires API key)
  - `DELETE /api/v1/courses/<id>/` (requires API key)

Authentication
- Read (`GET`) is open to everyone.
- Write (`POST/PUT/DELETE`) requires Tastypie API key authentication.
- Provide `username` and `api_key` either as query params or via the `Authorization` header (per Tastypie’s ApiKeyAuthentication).
- API keys are associated with Django users. If a user has no key yet, open the user in Django admin and save to trigger key creation (Tastypie’s signal) or use any available management command for key generation if present.

Course Fields (API)
- Required on create/update: `title` (str), `price` (float), `students_qty` (int), `reviews_qty` (int), `category_id` (int)
- Response excludes: `created_at`, `reviews_qty`
- Custom behavior:
  - hydrate: binds `category_id` to the `Course` instance
  - dehydrate: returns `category_id` and a simple `category` representation

Examples
- List courses (public):
  - `curl http://127.0.0.1:8000/api/v1/courses/?format=json`

- Create course (requires API key):
  - `curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"title":"Django Basics","price":49.0,"students_qty":100,"reviews_qty":10,"category_id":1}' \
    'http://127.0.0.1:8000/api/v1/courses/?username=<USER>&api_key=<API_KEY>&format=json'`

Focus Areas in This Project
- Clear separation between web views and API resources.
- Simple, expressive data model and admin UX (inlines, list displays).
- Demonstration of Tastypie with custom authentication rule: open reads, protected writes.
- Template structure with Bootstrap and clean navigation.

Notes
- If using a different database, update `DATABASES` in `base/settings.py`.
- Installed Django version in requirements is 4.0.8. Ensure your Python version is compatible.

