from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json

app = Flask(__name__, template_folder="")
socketio = SocketIO(app)
socketio.init_app(app)

responses = [{"init"}]


@app.route("/")
def index():
    return render_template("index.html", resps=responses)


@app.route("/requests", methods=["GET", "POST"])
def add_message():
    incoming = request.get_json()
    print(f"Incoming: {json.dumps(incoming)}")
    if incoming:
        print(f'Request dictionary: "{request.json}"')
        responses.append(request.json)
    else:
        print(f"Request: {request}")
    return json.dumps(incoming)


@app.after_request
def output(response):
    socketio.emit("my_response", request.get_json(silent=True), namespace="/")
    return response


socketio.run(
    app,
    host="0.0.0.0",
    port=81,
    debug=True,
    use_reloader=False,
    log_output=True,
    allow_unsafe_werkzeug=True,
)
