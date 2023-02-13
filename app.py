from flask import Flask, url_for, render_template
import traceback
import uuid

STATIC=False

app = Flask(__name__)


from routes import train, train_selector


def create_app():
    app = Flask(__name__)
    with app.app_context():
        print('hello')
    return app


if __name__ == '__main__':
    app.run()


def error_catcher():
    uuid_err = uuid.uuid4()
    print("Exception: " + str(uuid_err))
    traceback.print_exc()
    bs_css = url_for('static', filename='css/bootstrap.min.css')
    bs_js = url_for('static', filename='js/bootstrap.min.js')
    return render_template('error.html', uuid=uuid_err, bootstrapcss=bs_css, bootstrapjs=bs_js)
