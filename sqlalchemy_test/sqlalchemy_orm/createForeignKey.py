from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


#ORM精髓 relationship
from sqlalchemy.orm import relationship

BaseModel = declarative_base()

# 一对多
class School(BaseModel):
    __tablename__ = "school"
    id = Column(Integer,primary_key=True)
    name = Column(String(32), nullable=False)

class Student(BaseModel):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    sch_id = Column(Integer, ForeignKey("school.id"))

    # 关系映射
    stu2sch = relationship("School", backref="sch2stu")


# 链接数据库
from sqlalchemy_orm.sqlalchemy_engine import engine
BaseModel.metadata.create_all(engine)
