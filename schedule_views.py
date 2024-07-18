from flask import render_template, request, session, redirect, flash, url_for, Blueprint
from datetime import datetime

from models import User, Group,db

schedule_views = Blueprint('schedule_views',__name__,template_folder='templates')


@schedule_views.route('/list')
def list():
    return render_template('scheduler.html')
