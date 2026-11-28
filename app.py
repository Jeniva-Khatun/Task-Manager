
from flask import Flask, render_template
from database import get_all_tasks

app = Flask(__name__)


@app.route("/")
def home():
    tasks = get_all_tasks()
    return render_template("index.html", task=tasks)


if __name__ == "__main__":
    app.run(debug=True)