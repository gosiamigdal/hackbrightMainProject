from flask import Flask, render_template, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return redirect('/plans')

from app.plans.views import mod as plansModule
app.register_blueprint(plansModule)
