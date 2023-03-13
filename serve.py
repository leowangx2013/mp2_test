from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

# seed_number = [0]
proc = [None]
@app.route("/", methods=["GET", "POST"])
def serve():
    if request.method == 'POST':
        if proc[0] is not None:
            proc[0].terminate()
        data = request.get_json()
        print(data)
        usage = data['cpu_usage']
        if int(usage) == 0 and proc[0] is not None:
            proc[0].terminate()
            return "stop stressing CPU"
        else:
            proc[0] = subprocess.Popen(["stress-ng", "--cpu", "1", "--timeout", "0", "--cpu-load", str(usage)])
            hostname = socket.gethostname()
            return f"push EC2 instance {socket.gethostbyname(hostname)} to {usage}\% CPU usage"

    if request.method == 'GET':
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)