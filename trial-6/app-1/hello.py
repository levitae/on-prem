from flask import Flask
import socket

app = Flask(__name__)

@app.route('/hello')
def hello():
    hostname = socket.gethostname()
    return f'Hello from APP 1 and node {hostname}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
