from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = 'user_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card = Column(Integer, nullable=False, unique=True)
    lost_login = Column(DateTime, onupdate=datetime.now, default=datetime.now)
    login_num = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('user.id'))

    userdetail_for_foreignkey = relationship('User', backref='details', uselist=False, cascade='all')

    def __repr__(self):
        return '<UserDetails(id=%s,id_card=%s,lost_login=%s,login_num=%s,user_id=%s)>' % (
            self.id,
            self.id_card,
            self.lost_login,
            self.login_num,
            self.user_id
        )


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    creatime = Column(DateTime, default=datetime.now)
    username = Column(String(100), nullable=False)

    def __repr__(self):
        return '<User(id=%s,creatime=%s,username=%s)>' % (
            self.id,
            self.creatime,
            self.username,
        )


if __name__ == '__main__':
    from sqlalchemy import all_, any_
    # sqlite3数据库地址
    db = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path="test2.db")
    # sqlalchemy的引擎, echo=False不打印执行的SQL语句
    engine = create_engine(db, echo=False)
    # 会话类绑定引擎
    Session = sessionmaker(bind=engine)
    # 开启会话实例
    session = Session()
    Base.metadata.create_all(engine)

    # session.add_all([
    #     UserDetails(id_card=3, user_id=3),
    #     User(id=3, username="xx1")
    # ])

    session.commit()

