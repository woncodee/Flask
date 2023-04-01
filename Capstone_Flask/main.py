from flask import Flask,render_template,url_for
import sys
app = Flask(__name__)


@app.route("/")
def cctv():
    return render_template("cctv.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')