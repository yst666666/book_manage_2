# 数据库引擎的创建
from sqlalchemy.engine import create_engine
engine = create_engine('mysql+pymysql://root:123@127.0.0.1:3306/book_flask?charset=utf8')
