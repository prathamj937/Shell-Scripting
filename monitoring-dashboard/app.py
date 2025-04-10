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



