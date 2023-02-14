from __main__ import app
from flask import url_for, render_template


@app.route('/')
def selector():
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')

    return render_template('selector.html', bootstrapcss=bs_css, bootstrapjs=bs_js)
