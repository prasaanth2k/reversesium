from flask import Flask, render_template
from api.loadavg import loadaverage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/loadavg')
def api_loadavg():
    return loadaverage()

if __name__ == '__main__':
    app.run(port=4326, host='0.0.0.0')
