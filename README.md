# Grapes Task Manager

A small task management web app built with **Python** and **Flask**.

This project is a rebuild of my CS50-style Flask task manager — recreated from scratch to refresh fundamentals and iterate in public.

---

## Current Features

- Add tasks
- Edit tasks
- Mark tasks as completed
- Delete tasks
- Basic input validation (empty titles are rejected)

> Note: tasks are currently stored **in memory** (no database yet). Data resets when the server restarts.

---

## Tech Stack

- Python
- Flask
- Jinja2 templates
- HTML (server-side rendering)

---

## Roadmap
Planned next steps:

- Filter / hide completed tasks
- Duplicate task
- Categories (add / edit / delete)
- Persist data with SQLite
- UI improvements (CSS)
- Optional JS enhancements

---

## Run Locally

```bash
# create venv
python3 -m venv .venv
source .venv/bin/activate

# install deps
pip install -r requirements.txt

# run
python -m flask --app app run --port 5050
