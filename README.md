# 🍇 Grapes Task Manager

A small task management web application built with **Python** and **Flask**.

This project is a rebuild of a CS50-style Flask task manager, recreated from scratch to refresh core fundamentals and iterate in public.

---

## 🚀 Current Features

- Add tasks
- Edit tasks
- Mark tasks as completed
- Delete tasks
- Basic input validation (empty titles are rejected)

> ⚠️ **Note:** Tasks are currently stored **in memory** (no database yet).  
> Data resets when the server restarts.

---

## 🛠 Tech Stack

- Python
- Flask
- Jinja2 (server-side templates)
- HTML (server-side rendering)

---

## 🧭 Roadmap

Planned next steps:

- Filter / hide completed tasks
- Duplicate task functionality
- Task categories (add / edit / delete)
- Data persistence with SQLite
- UI improvements (CSS)
- Optional JavaScript enhancements

---

## ▶️ Run Locally

```bash
# create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the app
python -m flask --app app run --port 5050
