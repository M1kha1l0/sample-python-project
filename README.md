# ITMO superstudent blog (Django + SQLite)

Minimal Django blog:
- Public feed page (`/`)
- Post detail page (`/posts/<slug>/`)
- Admin panel for creating/editing posts (`/admin/`)

## Documentation

See `docs/README.md` for project documentation (setup, architecture, roadmap).

## Run locally

Create and activate a virtualenv (recommended), install dependencies, run migrations, create an admin user, then start the server.

```bash
cd /Users/ksabramov/ai/vibe

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Feed: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Create a post

1. Log into `/admin/`
2. Go to **Posts**
3. Click **Add Post**
4. Fill in title/content (slug auto-fills), keep **published** checked

Local development workspace.

## Haha

