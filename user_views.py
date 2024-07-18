from flask import render_template, request, session, redirect, flash, url_for, Blueprint
from datetime import datetime

from models import User, Group,db

user_views = Blueprint('user_views',__name__,template_folder='templates')

@user_views.route('/')
def index():
    return redirect(url_for('user_views.login'))
@user_views.route('/login')
def login():
    return render_template('login.html')

@user_views.route('/authenticate', methods=['POST'])
def authenticate():
    user = User.query.filter_by(cpf=request.form['cpf']).first()
    birth = datetime.strptime(request.form['birthdate'],'%Y-%m-%d')
    if user and (user.birthdate == birth):
        session['logged'] = user.id
        flash('Ola ' + user.name)
        return redirect(url_for('schedule_views.list'))
    else:
        flash ('Usuario nao encontrado')
        return redirect(url_for('user_views.login'))

@user_views.route('/newUser')
def newUser():
    return render_template('createuser.html', title='Novo Usuario')

@user_views.route('/createUser', methods=['POST'])
def createUser():
    name = request.form['name']
    cpf = request.form['cpf']
    birthdate = request.form['birthdate']
    email = request.form['email']
    phone = request.form['phone']

    user = User.query.filter_by(name=name).first()

    if user:
        flash('Usuario ja existe')
        return redirect(url_for('user_views.newUser'))

    new_user = User(name=name,cpf=cpf,birthdate=datetime.strptime(birthdate,'%Y-%m-%d'),email=email,phone=phone,registerdate=datetime.now())
    db.session.add(new_user)
    db.session.commit()

    flash('Usuario cadastrado com sucesso')
    return redirect(url_for('schedule_views.list'))
