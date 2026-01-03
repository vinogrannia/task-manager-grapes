from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

def add_task(title):
    task = {"title": title, "completed": False}
    tasks.append(task)

def get_tasks():
    return tasks

def check_if_index_valid(index):
    if index < 0 or index >= len(tasks):
        return False
    return True

def complete_task(index):
    if check_if_index_valid(index):
        tasks[index]["completed"] = True

def delete_task(index):
    if check_if_index_valid(index):
        tasks.pop(index)

@app.route("/")
def index():
    # временно добавим тестовые задачи, чтобы было что показать
    if not tasks:
        add_task("Buy milk")
        add_task("Walk the dog")
        complete_task(0)

    # пока просто покажем текстом, позже сделаем HTML
    return render_template("index.html", tasks=get_tasks())

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title").strip()
        if not title:
            return render_template("add.html", error="Title cannot be empty.")
        add_task(title)
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/complete/<int:index>", methods=["POST"])
def complete(index):
    complete_task(index)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    delete_task(index)
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if not check_if_index_valid(index):
        return redirect(url_for("index"))
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return render_template("edit.html", index=index, task=tasks[index], error="Title cannot be empty.")
        tasks[index]["title"] = title
    if request.method == "GET":
        task = tasks[index]
        return render_template("edit.html", index=index, task=task)
    return redirect(url_for("index"))



