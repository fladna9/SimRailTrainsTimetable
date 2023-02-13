import json
import datetime
from __main__ import app
from apiclient import dkfn_api
import requests
from flask import url_for, render_template
from app import STATIC, error_catcher


@app.route('/train/')
@app.route('/train/<number>')
def train(number=None):
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')

    # Setting a default train if none selected
    if not number or not str.isnumeric(number):
        return render_template('error-notrainnumber.html', bootstrapcss=bs_css, bootstrapjs=bs_js)

    # Getting static or API
    if STATIC:
        number = "24181"
        try:
            with open('examples/24181.json', 'r') as sample_file:
                stops = json.load(sample_file)
            data_is_from = "Static"
        except:
            return error_catcher()
    else:
        stops = dkfn_api.get_train(number)
        data_is_from = "API"

    # Building template
    return render_template('train.html', number=number, bootstrapcss=bs_css, stops=stops, bootstrapjs=bs_js,
                           datafrom=data_is_from)
