from flask import Flask
from models import db
from user_views import user_views
from schedule_views import schedule_views

app = Flask(__name__)
app.config.from_pyfile('./config.py')
app.register_blueprint(user_views)
app.register_blueprint(schedule_views)
db.init_app(app)


with app.test_request_context():

     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)