from flask import Flask
from os import getenv

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/1")
def hello_world1():
    return "<p>Hello</p>"

@app.route("/2")
def hello_world2():
    return "<p>Hello2</p>"

print(getenv("PORT_TEST"))

if __name__ == "__main__":
    print("Starting app")
    print(getenv("HOST_PORT"))
    print(getenv("HOST_ADDRESS"))
    print(getenv("DATABASE_URl"))
    print("#" * 100)
    app.run(debug=True, port=getenv("HOST_PORT"), host=getenv("HOST_ADDRESS"))
