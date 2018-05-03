from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hello Isabel Orticelle"


@app.route('/hello')
def user():
    import random

    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)


if __name__ == '__main__':
    app.run()
