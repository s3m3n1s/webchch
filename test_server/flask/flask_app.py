from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hi bro"


if __name__ == "__main__":
    app.run(port=int(8080))
