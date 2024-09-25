from flask import Flask, render_template, request
from api.controller import SessionController
import subprocess

app = Flask(__name__)

controller = SessionController()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_session", methods=["POST"])
def start_session():
    sessionname = request.form["sessionname"]
    hostname = request.form["hostname"]
    username = request.form["username"]
    network = request.form["network"] == "true"
    try:
        message = controller.start_session_with_network(
            sessionname, hostname, username, network
        )
    except subprocess.CalledProcessError as e:
        message = f"Error starting session: {e.output.decode()}"

    return render_template("index.html", message=message)

@app.route("/get_current_session", methods=["POST"])
def get_current_session():
    try:
        message = controller.get_current_running_session()
    except subprocess.CalledProcessError as e:
        message = f"Error getting current session: {e.output.decode()}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
