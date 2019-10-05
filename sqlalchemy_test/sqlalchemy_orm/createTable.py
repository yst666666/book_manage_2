from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
BaseModel = declarative_base()


# 创建表
class User(BaseModel):
    __tablename__ = 'user'

    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False, index=True, unique=True)


# 数据库引擎的创建
from sqlalchemy_orm.sqlalchemy_engine import engine


#利用 User 去数据库创建 user Table
BaseModel.metadata.create_all(engine)   # 数据库引擎
# 数据库呢? 数据库服务器地址呢?
# 数据库连接呢?