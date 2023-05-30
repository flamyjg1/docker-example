from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    return "<h1>i am from py web</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')