from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

BaseModel = declarative_base()


class Girl(BaseModel):
    __tablename__ = "girl"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    gyb = relationship("Boy", backref="byg", secondary="hotel")  # secondary="hotel" 数据表中的数据才能证明两者关系


class Boy(BaseModel):
    __tablename__ = "boy"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Hotel(BaseModel):
    __tablename__ = "hotel"
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, ForeignKey("boy.id"))
    gid = Column(Integer, ForeignKey("girl.id"))


from sqlalchemy_orm.sqlalchemy_engine import engine

BaseModel.metadata.create_all(engine)
