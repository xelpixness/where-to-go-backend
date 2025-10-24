# Where-to-Go Backend

Django backend for an interactive map application. Frontend based on [where-to-go-frontend](https://github.com/devmanorg/where-to-go-frontend).

🌳 Live demo: https://xelpix.pythonanywhere.com/

## Backend Tech Stack

- **Python 3.10** + **Django 4**
- **PostgreSQL** ready (SQLite for development)
- **Black** - code formatting
- **django-admin-sortable2** - drag & drop image sorting
- **django-ckeditor** - WYSIWYG content editing
- **python-decouple** - environment configuration
- **Pillow** - image processing

## Key Backend Features

- API endpoints for place data
- Admin interface with image previews and drag & drop
- WYSIWYG editor for HTML content
- Environment-based configuration
- Media file serving

## Quick Start

```bash
# 1. Clone & setup
git clone <repository-url>
cd palid-team-task
cp .env.example .env

# 2. Install & run
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```