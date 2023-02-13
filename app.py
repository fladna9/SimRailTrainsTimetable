from flask import Flask, url_for, render_template
import requests
import json
import traceback
import uuid

STATIC=False

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