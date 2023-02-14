import json
from __main__ import app
from apiclient import dkfn_api, static_api
from flask import url_for, render_template
from app import STATIC
from routes.error_handlers import error_catcher


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
        stops = static_api.get_train(number)
        data_is_from = "STATIC"
    else:
        stops = dkfn_api.get_train(number)
        data_is_from = "API"

    # Building template
    return render_template('train.html', number=number, bootstrapcss=bs_css, stops=stops, bootstrapjs=bs_js,
                           datafrom=data_is_from)
