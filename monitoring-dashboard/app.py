from flask import Flask, render_template, request, redirect, url_for,jsonify
import json
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/stats')
def get_stats():
    output = subprocess.check_output(['bash','system_stats.sh']).decode('utf-8')
    data = json.loads(output)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)



# FOR LINUX VM use the following app.py

from flask import Flask, render_template_string
import subprocess
import json

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html>
<head>
    <title>System Monitoring Dashboard</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body { font-family: Arial; background-color: #f4f4f4; padding: 2em; }
        .card { background: white; padding: 1.5em; margin: 1em auto; width: 300px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h2 { margin-top: 0; }
    </style>
</head>
<body>
    <div class="card">
        <h2>System Stats</h2>
        <p><strong>CPU:</strong> {{ stats['cpu'] }}%</p>
        <p><strong>Memory:</strong> {{ stats['memory'] }}</p>
        <p><strong>Disk:</strong> {{ stats['disk'] }}</p>
        <p><strong>Uptime:</strong> {{ stats['uptime'] }}</p>
    </div>
</body>
</html>
'''

@app.route('/')
def dashboard():
    try:
        output = subprocess.check_output(["./system_stats.sh"]).decode("utf-8")
        stats = json.loads(output)
    except Exception as e:
        stats = {"cpu": "N/A", "memory": "N/A", "disk": "N/A", "uptime": "N/A"}
    return render_template_string(TEMPLATE, stats=stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
