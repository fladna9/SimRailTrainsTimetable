import json
import traceback
import uuid
from __main__ import app
import requests
from flask import url_for, render_template
from app import STATIC, timetable_api


@app.route('/train/')
@app.route('/train/<number>')
def train(number=None):
    #Setting a default train if none selected
    if not number:
        number = "24181"

    #Getting static or API
    if STATIC:
        try:
            with open('examples/24181.json', 'r') as samplefile:
                stops = json.load(samplefile)
            dataisfrom = "Static"
        except:
            bs_css = url_for('static', filename='css/bootstrap.min.css')
            bs_js = url_for('static', filename='js/bootstrap.min.js')
            uuiderr = uuid.uuid4()
            print("Exception: " + str(uuiderr))
            traceback.print_exc()
            return render_template('error.html', uuid=uuiderr, bootstrapcss=bs_css, bootstrapjs=bs_js)

    else:
        timetable_response = requests.get(timetable_api + number)
        stops = timetable_response.json()
        dataisfrom = "API"

    #Making static files available
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')

    #Building template
    return render_template('train.html', number=number, stops=stops, bootstrapcss=bs_css, bootstrapjs=bs_js, datafrom=dataisfrom)
