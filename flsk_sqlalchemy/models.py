from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

BaseModel = declarative_base()


class Publisher(BaseModel):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    p_name = Column(String(32), nullable=False)


class Book(BaseModel):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    b_name = Column(String(32), nullable=False)
    pub_id = Column(Integer, ForeignKey('publisher.id', ondelete="CASCADE"))

    # 关系映射
    # 外键
    book_pub = relationship("Publisher", backref=backref("publisher", passive_deletes=True))


class Author(BaseModel):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    a_name = Column(String(32), nullable=False)

    a_b = relationship('Book', backref='b_a', secondary='book_author')


class BookAuthor(BaseModel):
    __tablename__ = "book_author"
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, ForeignKey("book.id"))
    aid = Column(Integer, ForeignKey("author.id"))


from sqlalchemy_engine import engine

BaseModel.metadata.create_all(engine)
