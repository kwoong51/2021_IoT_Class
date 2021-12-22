from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
        <p>Hello, Flask!</p>
        <a href="/first">Go first</a>
        <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first_page():
    return '''
        <p>First Page</p>
        <a href="/">Go home</a>
    '''

@app.route("/second")
def Second_page():
    return '''
        <p>Second Page</p>
        <a href="/">Go home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")