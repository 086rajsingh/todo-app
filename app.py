from flask import Flask, render_template, request, redirect

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

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)