from todoapp.models.models import Task
from flask import Blueprint, render_template, request, redirect, url_for


todo_bp = Blueprint('todo', __name__)

tasks = []


@todo_bp.route('/')
def index():
    return render_template("index.html", tasks=tasks)


@todo_bp.route('/add', methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        tasks.append(Task(title=title))
    return redirect(url_for("todo.index"))


@todo_bp.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id].completed = True
    return redirect(url_for("todo.index"))
