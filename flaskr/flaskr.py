from flask import Flask
from flask import request, render_template, redirect, url_for


app = Flask(__name__) # create the application instance :)


@app.route("/add/<int:num1>/<float:num2>")
@app.route("/add/<float:num1>/<float:num2>")
@app.route("/add/<float:num1>/<int:num2>")
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    context = {'num1':num1, 'num2':num2}
    return render_template("add.html", **context)

# web logic starts here
@app.route("/") # bind the uri to the index function 
def index(name='Flaskr'):
    return render_template("index.html", name = name)


@app.route('/success/<name>')
def success(name):
    return render_template("success.html", name = name)


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')