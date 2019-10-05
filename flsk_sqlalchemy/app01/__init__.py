from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app01.views.publisher import publisher

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SESSION_COOKIE_NAME'] = 'i am not session'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/book_flask?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #  注册蓝图
    app.register_blueprint(publisher)

    db.init_app(app=app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run('127.0.0.1', 9527)
