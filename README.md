# Django Revision Workspace

This repository is a personal Django revision folder made up of many small,
independent practice projects. Each subfolder is its own mini app or Django
project, covering common topics like CRUD, templates, forms, authentication,
media uploads, middleware, signals, and REST APIs.

## What Is In Here

The workspace includes multiple standalone Django projects such as:

- `myProject1` to `myProject30`
- `apiProject01` to `apiProject05`
- `django`
- `django1`

Most of these folders follow the standard Django layout:

- `manage.py`
- a project package such as `myProject16/` or `apiProject05/`
- one or more apps such as `blog/`, `accounts/`, `student/`, `portfolio/`,
  `shop/`, `api/`, or `youtube/`

## Topics Covered

Across the different practice projects, the repository appears to include work on:

- basic Django project setup
- URL routing and views
- templates and template inheritance
- models and migrations
- forms and model forms
- CRUD workflows
- authentication and account management
- profile upload and media handling
- Django messages framework
- sessions and middleware
- signals
- email templates
- Django REST Framework style APIs

## Project Highlights

Here are a few of the more recognizable practice areas from the folder names and
file structure:

- `myProject13` - student CRUD-style app with forms and templates
- `myProject14` - messages framework demo
- `myProject16`, `myProject17`, `myProject26` - authentication, accounts, and
  profile features
- `myProject20`, `myProject24`, `myProject25`, `myProject29`, `myProject30` -
  blog and user-related CRUD examples
- `myProject21`, `myProject22` - middleware and signals practice
- `myProject28` - user list / youtube-themed practice app
- `apiProject01` to `apiProject05` - API and serializer practice

## How To Run A Project

Each project is independent, so work inside the folder you want to run.

```powershell
cd .\myProject13
python manage.py migrate
python manage.py runserver
```

If the project has new models or migrations, run:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Setup Notes

- Activate your virtual environment before running Django commands.
- The repository `.gitignore` excludes common local files such as virtual
  environments, `__pycache__`, `.env`, and `db.sqlite3`.
- Some API projects may need extra packages such as `djangorestframework`.

## Recommended Way To Explore

If you are revising Django, a good order is:

1. Start with a basic project folder.
2. Review `views.py`, `urls.py`, and templates.
3. Move on to models, forms, and migrations.
4. Practice auth, media, messages, sessions, middleware, and signals.
5. Finish with the API projects.

## Notes

This repo is best treated as a collection of practice snapshots rather than one
single production app. Each folder can be opened on its own and studied
independently.
