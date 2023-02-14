from __main__ import app
from flask import render_template


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")