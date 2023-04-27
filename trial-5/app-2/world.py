from flask import Flask
import socket

app = Flask(__name__)

@app.route('/world')
def world():
    hostname = socket.gethostname()
    return f'World! from APP 2 and node {hostname}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
