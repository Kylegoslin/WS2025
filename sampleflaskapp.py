from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "This is the root page."
    
    
@app.route("/hello1")
def hello1():
    return "hello1"

@app.route("/hello2")
def hello2():
    return "hello2"

@app.route("/hello3")
def hello3():
    return "hello3"

@app.route("/hello4")
def hello4():
    return "hello4"

if __name__ == "__main__":
    app.run(debug=True)

