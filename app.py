from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    # return "Hello world"
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    email = request.form['email']
    contact = request.form['contact']

    print(name)
    print(email)
    print(contact)
    # return render_template('pass.html', n=name, e=email, c=contact)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
