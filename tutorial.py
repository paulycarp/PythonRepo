from flask import Flask

app  = Flask(__name__)

@app.route("/")
def home():
    return "Hello! World I am new here<h1>Hello<h1>"

if __name__ == "__main__":
    app.run()