from flask import (
    Flask, request, render_template, 
    redirect, url_for
)
# from flaskr.utils import get_instance_folder_path
# from flaskr.cache import cache
# from flaskr.config import configure_app
# from flaskr.data.models import db


# app = Flask(__name__,
#             instance_path=get_instance_folder_path(),
#             instance_relative_config=True,
#             template_folder='templates')

app = Flask(__name__,
    template_folder='templates',
    static_folder = "static")


# configure_app(app)
# cache.init_app(app)
# db.init_app(app)


# web logic starts here
@app.route("/") # bind the uri to the index function 
def index():
    return render_template("index.html")


@app.route('/results')
def results():
    return render_template("results.html")


@app.route('/login', methods=['POST','GET'])
def login():
    return redirect(url_for('results'))



if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')