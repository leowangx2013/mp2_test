from flask import Flask, request

app = Flask(__name__)

seed_number = [0]
@app.route("/", methods=["GET", "POST"])
def serve():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        seed_number[0] = data['num']
        return "success"
    if request.method == 'GET':
        return str(seed_number[0])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
