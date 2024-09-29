from flask import Flask, render_template, request, jsonify
from lib.deployers import Deployers

app = Flask(__name__)
deploy = Deployers()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/startsession", methods=["POST"])
def startsession():
    try:
        session_name = request.form["sessionname"]
        hostname = request.form["hostname"]
        network = request.form["network"]
        username = request.form["username"]
        output = deploy.startsession(session_name, hostname, network, username)
        return jsonify({"output": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/runningsessions",methods=['POST'])
def runningsession():
    try:
        output = deploy.currentsession()
        return jsonify({"output":output}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500
if __name__ == "__main__":
    app.run(debug=True)
