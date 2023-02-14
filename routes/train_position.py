from flask import url_for, render_template
from apiclient.simrail_official_api import get_trains_list
from __main__ import app


@app.route('/trains-list/<server_name>')
def trains_list(server_name=None):
    if server_name is None:
        app.error_catcher()
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')

    return get_trains_list(server_name)
