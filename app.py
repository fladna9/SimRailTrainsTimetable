from flask import Flask, url_for, render_template
import requests

app = Flask(__name__)

timetable_api="https://sr-dispatch-api-staging-uld3cp3nxa-od.a.run.app/train/"

url_for('static', filename='css/bootstrap.min.css')
url_for('static', filename='js/bootstrap.min.js')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/train/')
@app.route('/train/<number>')
def train(number=None):
    if not number:
        number = "24181"
    timetable_response = requests.get(timetable_api + number)
    stops = timetable_response.json()
    return render_template('train.html', number=number, stops=stops)
if __name__ == '__main__':
    app.run()
