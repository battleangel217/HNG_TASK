# HNG_TASK

This repository contains a small Django project that exposes a simple API endpoint returning a profile and a cat fact fetched from an external API.

## Contents

- A Django project in `HNG/`
- An app `MyProfile/` which implements the profile API
- `requirements.txt` listing Python dependencies
- `db.sqlite3` (default SQLite database)

## Prerequisites

- Linux / macOS / Windows with WSL
- Python 3.12 (project was developed with Python 3.12)
- pip (comes with Python)

If you'd rather use the included virtual environment (not recommended for development), there's an `env/` directory in the repo that can be activated. For development it's better to create an isolated venv.

## Quick setup (recommended)

Open a terminal and run:

```bash
# clone the repo (if you haven't already)
git clone <your-repo-url>
cd HNG1

# create and activate a virtual environment (Linux / macOS)
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# apply migrations (SQLite is configured by default)
python manage.py migrate

# run the development server
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/api/me/

Optional: activate the included venv instead of creating a new one:

```bash
source env/bin/activate
```

## Dependencies

All Python dependencies are listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt
```

Key dependencies used by the project:

- Django
- djangorestframework (DRF)
- requests (used to fetch a cat fact from https://catfact.ninja)

See `requirements.txt` for exact pins.

## Environment & notes

- The API endpoint makes an outbound HTTP request to `https://catfact.ninja/fact`. Ensure the machine running the server has internet access for the endpoint to return the cat fact.
- No additional environment variables are required to run this project in development. For production you should set `SECRET_KEY`, `DEBUG=False` and configure an appropriate database.

## API docs

Detailed API documentation for the profile endpoint is available in `API_DOCUMENTATION.md` in the repository root.

## Troubleshooting

- If you see errors while installing packages, make sure you are using the correct Python version (3.12) and that pip is up to date.
- If the external catfact service is unreachable, the API will return an error response. See `API_DOCUMENTATION.md` for the error codes the view may return.

## Tests

No automated tests are included in this repository at the moment. You can manually exercise the endpoint via curl or a browser.


