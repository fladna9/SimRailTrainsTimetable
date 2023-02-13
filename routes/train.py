import json
import traceback
import uuid
import datetime
from __main__ import app

import requests
from flask import url_for, render_template
from app import STATIC, timetable_api, ErrorCatcher


@app.route('/train/')
@app.route('/train/<number>')
def train(number=None):
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')

    #Setting a default train if none selected
    if not number or not str.isnumeric(number):
        return render_template('error-notrainnumber.html', bootstrapcss=bs_css, bootstrapjs=bs_js)

    #Getting static or API
    if STATIC:
        number = "24181"
        try:
            with open('examples/24181.json', 'r') as samplefile:
                stops = json.load(samplefile)
            dataisfrom = "Static"
        except:
            return ErrorCatcher()

    else:
        try:
            timetable_response = requests.get(timetable_api + number)
            stops = timetable_response.json()
            dataisfrom = "API"
        except:
            return ErrorCatcher()

    for stop in stops:
        if stop['stop_type'] and stop['scheduled_arrival_hour']:
            if stop['layover']:
                stop['departure_time'] = (datetime.datetime.strptime(stop['scheduled_arrival_hour'], '%H:%M') + datetime.timedelta(minutes=float(stop['layover']))).time().strftime("%H:%M")
            else:
                stop['departure_time'] = stop['scheduled_arrival_hour']

    #Building template
    return render_template('train.html', number=number, bootstrapcss=bs_css, stops=stops, bootstrapjs=bs_js, datafrom=dataisfrom)
