#!/usr/bin/env python3

import os
import json

from voting import config
from sqlalchemy.sql import func
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, render_template, request, make_response, current_app


app = Flask(__name__, template_folder='templates', static_folder='static')
config.configure_app(app)

db = SQLAlchemy(app)

# datamodel
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    action = db.Column(db.String(10))
    value = db.Column(db.Integer(), default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, action, value, created_at):
        self.username = username
        self.action = action
        self.value = value
        self.created_at = created_at



# web logic starts here
@app.route("/") # bind the uri to the index function 
def index():
    return render_template("index.html")


@app.route('/ce-results', methods=['POST','GET'])
def handle_data():
    if request.method == 'POST':
        result = dict(request.form) # {'click': ['{"username":"Mr.Potato","value":1}']}
        click_data = json.loads(result['click'][0]) # {'username': 'Mr.Potato', 'value': 1}

        user = User(click_data['username'],'Click',1, datetime.now())
        db.session.add(user)
        db.session.commit()
        current_app.logger.info('A record was successfully added: {}'.format(click_data))

        #[('Mr.Judge', 4), ('Mr.Potato', 5), ('Mrs.Lam', 5)]
        query_res = db.session.query(User.username, func.sum(User.value)).group_by(User.username).all()
        user_list = [user[0] for user in query_res]
        data = [user[1] for user in query_res]

        response = make_response(render_template("results.html", 
            click_data=click_data, 
            data=data, 
            user_list=user_list))

        current_app.logger.info("Response sent")

        return response




