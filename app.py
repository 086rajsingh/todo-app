from flask import Flask, render_template, request, redirect
<<<<<<< HEAD
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()

    if request.method == "POST":
        task = request.form["task"]
        if task:
            db.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            db.commit()

    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (id,))
    db.commit()
=======

app = Flask(__name__)

# File ka naam
FILE_NAME = "tasks.txt"


# Tasks load karne ka function
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.read().splitlines()
    except:
        tasks = []
    return tasks


# Tasks save karne ka function
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


@app.route("/", methods=["GET", "POST"])
def home():
    tasks = load_tasks()

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
            save_tasks(tasks)
        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

>>>>>>> f4e125189605e96fc7c451f35dc1751e23c5cba3
    return redirect("/")


if __name__ == "__main__":
<<<<<<< HEAD
    app.run()
=======
    app.run(debug=True)
>>>>>>> f4e125189605e96fc7c451f35dc1751e23c5cba3
