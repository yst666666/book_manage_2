from app01 import db


# db.Model 就是==BaseModel ==使用SQLAlchemy

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


if __name__ == '__main__':
    #  create_app 配置好config的app
    from app01 import create_app

    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)
