from flask import Flask, render_template, request, redirect, url_for
from db import initialize_db, add_task, get_tasks, get_task, complete_task, delete_task, edit_task
import db

app = Flask(__name__)

initialize_db()

@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title").strip()
        if not title:
            return render_template("add.html", error="Title cannot be empty.")
        add_task(title)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = get_task(task_id)
    if task is None:
        return "Task not found", 404
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return render_template("edit.html", id=task_id, task=task, error="Title cannot be empty.")
        edit_task(task_id, title)
        return redirect(url_for("index"))
    if request.method == "GET":
        return render_template("edit.html", id=task_id, task=task)



