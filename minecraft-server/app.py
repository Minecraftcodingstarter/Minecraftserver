from flask import Flask, render_template, request, redirect
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_server():
    script_path = os.path.abspath("start.bat")
    subprocess.Popen(["cmd", "/c", script_path], shell=True)
    return redirect('/')

@app.route('/stop', methods=['POST'])
def stop_server():
    script_path = os.path.abspath("end.bat")
    subprocess.Popen(["cmd", "/c", script_path], shell=True)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
