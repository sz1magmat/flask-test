from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="159.69.179.95")