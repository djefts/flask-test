# Flask Test Server

This is a simple Python application to help with testing an HTTP Requests service. After starting the server, any HTTP Requests sent to the server will be displayed on the webpage immediately.

## Setup
```shell
pip install flask flask_socketio
```

## Use
1. Run `app.py`
2. Go to `localhost:81` in your favorite browser
3. Send an HTTP Request (`GET` or `POST`) to `localhost:81/requests`
