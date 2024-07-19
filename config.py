import os

print(os.getenv('SECRET_KEY'))
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///scheduler.db'