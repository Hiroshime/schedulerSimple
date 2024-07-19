from flask import render_template, request, session, redirect, flash, url_for, Blueprint
import datetime

from models import Session

schedule_views = Blueprint('schedule_views',__name__,template_folder='templates')


@schedule_views.route('/list')
def list_sessions():
    five_days = datetime.datetime.now() + datetime.timedelta(days=5)
    today = datetime.datetime.now()
    sessions = Session.query.filter(Session.schedule <= five_days).filter(Session.schedule >= datetime.datetime.now())

    return render_template('scheduler.html', today=today, sessions=sessions)
