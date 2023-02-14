from flask import Flask, url_for, render_template
import traceback
import uuid

STATIC=False

app = Flask(__name__)


from routes import train, \
    train_selector, \
    train_position, \
    error_handlers


def create_app():
    app = Flask(__name__)
    with app.app_context():
        print('hello')
    return app


if __name__ == '__main__':
    app.run()

