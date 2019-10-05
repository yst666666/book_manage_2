from flask import Blueprint

from app01.models import db, Users

user = Blueprint('user', __name__)


@user.route('/reg/<username>')
def reg(username):
    # 给Users表中添加数据
    u = Users(name=username)
    #
    db.session.add(u)
    db.session.commit()

    return 'reg 200ok!'


@user.route('/user_list')
def user_list():
    res = Users.query.filter().all()
    print(res)

    return f'当前有{len(res)}个用户'
