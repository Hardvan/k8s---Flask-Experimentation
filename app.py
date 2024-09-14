from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """<h1>Hello, World!</h1>
This is a simple Flask web application that is running inside a Docker container and deployed on a Kubernetes cluster.
"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
