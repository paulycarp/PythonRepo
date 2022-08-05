from flask import Flask, redirect, url_for

app  = Flask(__name__)

@app.route("/")
def index():
    return "Hello! World I am new here. Thank. <h1>Hello<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

    @app.route("/admin")
    def admin():
        return redirect(url_for("user", "Admin!"))

if __name__ == "__main__":
    app.run()