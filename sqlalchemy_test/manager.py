# 启动Flask

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app01 import create_app, db

# Migrate --manager 初始化

# 配置好config的app
app = create_app()

mig = Migrate(app, db)
# 把配置好的app放入Manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)
"""
Flask-Migrate  依赖组件Flask-Script
"""


# python manager.py db runserver
# python manager.py db init  初始化数据库
# python manager.py db migrate ----django 的makemigrations
# python manager.py db upgrade  ----django 的migrate

@manager.command
def oldboys21(args):
    print(args)
    return args


@manager.option('-w', '--who', dest='who')
@manager.option('-s', '--sss', dest='sss')
def func(who, sss):
    print(f"{who},你好{sss}")


if __name__ == '__main__':
    # app.run('127.0.0.0',9527)
    manager.run()
