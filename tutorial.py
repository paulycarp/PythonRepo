from flask import Flask

app  = Flask(__main__)

@app.route("/")
def home():
    return "Hello! World <h1>Hello<h1>"

if __name__ == "__main__":
    app.run()