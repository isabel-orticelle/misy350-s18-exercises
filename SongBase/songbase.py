from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hello friend"


@app.route('/user')
def user():
    return "this is a user page"


if __name__ == '__main__':
    app.run()
