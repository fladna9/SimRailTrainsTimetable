import traceback
import uuid
from __main__ import app
from flask import render_template, url_for


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


def error_catcher():
    uuid_err = uuid.uuid4()
    print("Exception: " + str(uuid_err))
    traceback.print_exc()
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')
    return render_template('error.html', uuid=uuid_err, bootstrapcss=bs_css, bootstrapjs=bs_js)