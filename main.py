from flask import Flask,render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
# from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    print("Received Message",message)
    if message != "User Connected!":
        send(message,broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app,host='0.0.0.0',allow_unsafe_werkzeug=True,port=5000)