#!/usr/bin/env python3

import os
import json

from voting import config
from sqlalchemy.sql import func
from sqlalchemy import text
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


def get_last_10_mins_data():
    sql_text = (
    """
    SELECT 
        username, 
        CAST((JulianDay(Datetime('now','localtime')) - JulianDay(created_at)) * 24 * 60 As Integer),
        sum(value)
    FROM user 
    WHERE created_at >= Datetime('now', '-10 minutes','localtime')
    AND created_at < Datetime('now','localtime')
    GROUP BY 1,2
    """)
    agg_result = db.engine.execute(sql_text)

    data_dict ={
        "Mr.Judge":{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0},
        "Mr.Potato":{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0},
        "Mrs.Lam":{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    }
    for row in agg_result:
        user = row[0]
        time_mins = row[1]
        value = row[2]
        data_dict[user][time_mins] = value

    data = [list(val.values()) for val in data_dict.values()]
    return data


def get_sum_data():
    #[('Mr.Judge', 4), ('Mr.Potato', 5), ('Mrs.Lam', 5)]
    query_res = db.session.query(User.username, func.sum(User.value)).group_by(User.username).all()
    user_list = [user[0] for user in query_res]
    data = [user[1] for user in query_res]
    return (user_list, data)



@app.route('/ce-results', methods=['POST','GET'])
def handle_data():
    if request.method == 'POST' and request.method:
        result = dict(request.form) # {'click': ['{"username":"Mr.Potato","value":1}']}
        click_data = json.loads(result['click'][0]) # {'username': 'Mr.Potato', 'value': 1}

        user = User(click_data['username'],'Click',1, datetime.now())
        db.session.add(user)
        db.session.commit()
        current_app.logger.info('A record was successfully added: {}'.format(click_data))

        sum_data = get_sum_data()
        period_data = get_last_10_mins_data()

        response = make_response(render_template("results.html", 
            data=sum_data[1], 
            user_list=sum_data[0],
            agg_data=period_data)
        )

        current_app.logger.info("POST Response sent")
        return response
    else:
        sum_data = get_sum_data()
        period_data = get_last_10_mins_data()
        response = make_response(render_template("results.html", 
            data=sum_data[1], 
            user_list=sum_data[0],
            agg_data=period_data)
        )
        current_app.logger.info("GET Response sent")
        return response




