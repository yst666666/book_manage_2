from flask import Blueprint, render_template, redirect, request
from sqlalchemy.orm import sessionmaker

from models import Publisher
from sqlalchemy_engine import engine

publisher = Blueprint('publisher', __name__)

select_db = sessionmaker(engine)
db_session = select_db()


@publisher.route('/pub_list/')
def pub_list():
    pub_all = db_session.query(Publisher).all()
    print(pub_all)
    return render_template('publish/publish_list.html', pub_all=pub_all)


@publisher.route('/pub_add/', methods=['GET', 'POST'])
def pub_add():
    if request.method == 'POST':
        pub_obj = request.form.to_dict()
        print(pub_obj)
        pub_name = pub_obj.get('p_name')
        pub_obj = Publisher(p_name=pub_name)
        db_session.add(pub_obj)
        db_session.commit()
        db_session.close()
        return redirect('/pub_list')
    return render_template('publish/publish_add.html')


@publisher.route('/pub_edit/<pid>', methods=['GET', 'POST'])
def pub_edit(pid):
    if request.method == 'POST':
        pub_obj = request.form.to_dict()
        db_session.query(Publisher).filter(Publisher.id == pid).update(pub_obj)
        db_session.commit()
        db_session.close()
        return redirect('/pub_list')
    pub_obj = db_session.query(Publisher).filter(Publisher.id == pid).first()
    return render_template('publish/publish_edit.html', pub_obj=pub_obj)


@publisher.route('/pub_del/<pid>')
def pub_del(pid):
    print(pid)
    db_session.query(Publisher).filter(Publisher.id == pid).delete()
    db_session.commit()
    # db_session.close()
    return redirect('/pub_list/')
