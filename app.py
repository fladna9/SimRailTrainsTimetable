from flask import Flask, url_for, render_template
import requests
import json
import traceback
import uuid

STATIC=True

app = Flask(__name__)
timetable_api = "https://sr-dispatch-api-staging-uld3cp3nxa-od.a.run.app/train/"


from routes import train, trainselector

def create_app():
    app = Flask(__name__)

    with app.app_context():
        print('hello')
    return app

if __name__ == '__main__':
    app.run()


def ErrorCatcher():
    uuiderr = uuid.uuid4()
    print("Exception: " + str(uuiderr))
    traceback.print_exc()
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')
    return render_template('error.html', uuid=uuiderr, bootstrapcss=bs_css, bootstrapjs=bs_js)