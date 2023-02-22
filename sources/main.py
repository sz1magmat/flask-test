from flask import Flask

app = Flask(__name__)

@app.route("/1")
def hello_world1():
    return "<p>Hello</p>"

@app.route("/2")
def hello_world2():
    return "<p>Hello2</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
