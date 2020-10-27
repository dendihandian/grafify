from flask import Flask, render_template
from config.app import APP_DEBUG

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=APP_DEBUG)
