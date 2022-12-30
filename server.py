from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("base.html")

@app.route("/contacto")
def contacto():
    return render_template("base.html")

@app.route("/admin")
def admin():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)    # Run in debug mode