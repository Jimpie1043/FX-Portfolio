
# FX Portfolio

**This repo is a work in progress.** It will be used as a portfolio to demonstrate my technical documentation and projects.
## Table of Contents

- [Tech Stack](#tech-stack)

- [Current Goals](#current-1-10-goals)

- [Completed Goals](#completed-goals)

- [Environment Variables](#environment-variables)

- [Development Setup](#development-setup)

- [Development Workflow](#development-workflow)

- [Production Build](#production-build)
## Tech Stack

**Frontend:** HTML, Tailwind CSS, TypeScript

**Backend:** Python, Django

**Database:** PostgreSQL (Docker container)

**Tools:** Docker Compose, Git, npm
## Environment Variables

The following environment variables are needed for the website to work.

### PostgreSQL

`POSTGRES_DB`

`POSTGRES_USER`

`POSTGRES_PASSWORD`

`POSTGRES_HOST`

`POSTGRES_PORT`

### Django

`SECRET_KEY`

`DJANGO_SETTINGS_MODULE` Set to: config.settings.dev/prod/testing
## Development Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create and Activate the Virtual Environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Node Dependencies

```bash
npm install
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add the required environment variables.

### 6. Start the PostgreSQL Database

```bash
docker compose up -d
```

### 7. Apply Database Migrations

```bash
python manage.py migrate
```
## Development Workflow

After the initial setup, run the following processes:

#### Terminal 1 — PostgreSQL

If not already started:

```bash
docker compose up -d
```

#### Terminal 2 — Tailwind CSS

```bash
npm run dev:css
```

#### Terminal 3 — TypeScript

```bash
npm run dev:ts
```

Tailwind CSS and TypeScript run in watch mode during development and automatically rebuild when their source files change.

#### Terminal 4 — Django

```bash
python manage.py runserver
```

Or to make the website available from other devices in your LAN.

```bash
python manage.py runserver 0.0.0.0:8000
```

The website will be available at `http://127.0.0.1:8000/` for local access from the machine or `http://<LAN_IP>:8000/` for other devices.
## Production Build

To build the frontend assets without watch mode:

```bash
npm run build
```

This generates the production Tailwind CSS and compiled TypeScript output.