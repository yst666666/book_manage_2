# 模拟 navcat 操作
# 1. 选择数据库
from sqlalchemy_orm.sqlalchemy_engine import engine

# 2. 选择表
# 3.创建查询窗口
from sqlalchemy.orm import sessionmaker

# 选中数据库
select_db = sessionmaker(engine)
# 打开查询窗口
db_session = select_db()

# 4. 写入SQL语句
from sqlalchemy_orm.createTable import User

"""
添加数据
"""
# user_list = [User(name='吴建伟'),User(name='杨苏婷'),User(name='杨苏东')]
#
# # 放入查询的窗口
# # db_session.add(user)
# db_session.add_all(user_list)
# # 提交sql语句
# db_session.commit()
#
# # 关闭查询窗口
# db_session.close()

"""
简单无条件查询
select * from user  table_user == class_User
"""
# 查询全部符合条件的数据
# res = db_session.query(User).all()
# for i in res:
#     print(i.id,i.name)

"""
1 吴建伟
3 杨苏东
2 杨苏婷
"""
"""
简单条件查询
select * from user where id=3
"""
# res1 = db_session.query(User).filter(User.id == 3).all()
# print(res1[0].id,res1[0].name)
"""
3 杨苏东
"""

# # filter_by 等同于上面的方法
# res3 = db_session.query(User).filter_by(id=3).all()
# print(res3[0].id,res3[0].name)
#
# res4 = db_session.query(User).filter(User.id == 3 and User.name == "123").all()
# # and 可以找到答案
# res4 = db_session.query(User).filter(User.id == 3, User.name == "123").all()
# # , 取到的是空列表
# print(res4)








"""
修改数据 update
"""

# res = db_session.query(User).filter(User.id == 1).update({"name":"李亚历山大"})
# db_session.commit()
# db_session.close()

"""
删除数据
"""
# res = db_session.query(User).filter(User.id == 2).delete()
# db_session.commit()
# db_session.close()

