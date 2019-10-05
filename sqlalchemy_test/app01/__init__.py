
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 实例化 SQLAlchemy
db = SQLAlchemy()

from app01.views import user



def create_app():
    # 实例化 Flask
    app = Flask(__name__)
    # 配置 app.config
    app.config['DEBUG'] = True
    app.config['SESSION_COOKIE_NAME'] = 'i am not session'
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/s21_sqlalchemy?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 注册蓝图
    app.register_blueprint(user.user)

    # 把实例化的Flask==app 放到 实例化的SQLAlchemy==db 里面
    db.init_app(app=app)
    return app
