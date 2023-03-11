from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

# seed_number = [0]
proc = None
@app.route("/", methods=["GET", "POST"])
def serve():
    if request.method == 'POST':
        if proc is not None:
            proc.terminate()
        data = request.get_json()
        print(data)
        usage = data['cpu_usage']
        proc = subprocess.Popen(["stress-ng", "--cpu", "1", "--cpu-load", str(usage)])
        hostname = socket.gethostname()
        return f"push {socket.gethostbyname(hostname)} to {usage}"
    
    if request.method == 'GET':
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
