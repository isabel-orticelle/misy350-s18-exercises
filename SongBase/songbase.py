from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return "hello friend"
    return render_template('index.html')


@app.route('/users/<string:username>')
def users(username):
    #return "<h1>hello %s</h1>" % username
    return render_template('user.html', uname=username)


@app.route('/user')
def user():
    return "this is a user page"


@app.route('/form-basics')
def form_basics():
        # return "hello friend"
    return render_template('form-basics.html')


@app.route('/form-demo')
def form_demo():
        # return "hello friend"
    first_name=request.args.get('first_name')
    return first_name


if __name__ == '__main__':
    app.run()
