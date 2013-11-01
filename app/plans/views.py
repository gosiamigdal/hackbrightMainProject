from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.plans.models import Plan

mod = Blueprint('plans', __name__, url_prefix='/plans')

@mod.route("/")
def index():
    plans = Plan.query.all()
    return render_template("plans/index.html", plans=plans)
