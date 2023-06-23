from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean, DateTime, ForeignKey
from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship

Models = declarative_base()


class db(object):
    Models = declarative_base()


"""表类创建区"""


""""""

if __name__ == '__main__':
    # 数据库地址
    db = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path="test.db")
    # sqlalchemy的引擎
    engine = create_engine(db, echo=True)
    # 创建表
    Models.metadata.create_all(engine)
    # 会话类绑定引擎
    Session = sessionmaker(bind=engine)
    # 开启会话实例
    session = Session()
    """测试区"""

    """"""
    # 提交至数据库
    session.commit()
    # 关闭会话
    session.close()
