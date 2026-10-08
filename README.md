# Flask Final Assignment

A starter REST API for the Coventry University Web Development coursework. It uses Flask's application factory pattern, Flask-SQLAlchemy, and Flask-Migrate, with PostgreSQL configuration ready for future models. The initial API contains a health check at `GET /api/health`.

## Local setup

Use Python 3.9 or newer. From the project root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Environment variables

Copy `.env.example` to `.env` and replace its placeholder values with local settings. Keep `.env` private and out of version control.

```bash
cp .env.example .env
```

Set `SECRET_KEY` to a random secret value and set `DATABASE_URL` to your PostgreSQL connection URL. The example URL uses the `postgresql+psycopg` driver. Until `DATABASE_URL` is set, the app uses a local SQLite database so the starter endpoint can run without PostgreSQL.

## Run the application

```bash
flask --app wsgi run --debug
```

The health endpoint is available at <http://127.0.0.1:5000/api/health>.

## Run tests

```bash
python -m pytest
```

## Production server

With the virtual environment activated and production environment variables configured, run:

```bash
gunicorn wsgi:app
```
