from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship

Models = declarative_base()

"""表类创建区"""


# 文章作者表 多对一
class User(Models):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    # articles = relationship('Article', backref='users')


# hhy sqlalchemy， Article对User 多对一
class Article(Models):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String, nullable=False)
    # yyh sqlalchemy中 外键一般设在多对一中的多中，或多对多中的外键表中
    author_id = Column(Integer, ForeignKey('user.id'))
    # yyh sqlalchemy中 反向查询关系属于一种属性,一般建立在外键对应的类中，也可以在外键在的类中，
    # yyh relationship这个属性中， backref参数代表所在类的表名， 第一参数是对应的正查询类的类名
    author = relationship('User', backref='articles')


class ClassStudent(Models):
    __tablename__ = 'class_student'
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)


class Class(Models):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # yyh sqlalchemy中 relationship是存在于类属性中， 和外键不同，外键存在于数据库表中，
    # yyh back_populates，用于多对多的逆向查询， 而backref，用于一对多的你查下
    students = relationship("Student", secondary="class_student", back_populates="classes")
    name = Column(String(1024))


class Student(Models):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)
    classes = relationship("Class", secondary="class_student", back_populates="students")
    name = Column(String(1024))

    # 设置索引
    # id = Column(db.Integer, primary_key=True)  # 主键索引
    # address = Column(db.String(11), index=True)   # 普通索引
    # phone = Column(db.String(11), unique=True)    # 唯一约束

    # 联合索引/复合索引, 元组结构
    # from sqlalchemy import Index
    # __table_args__ = (
    #     Index('ser_cre', "server_id", "create_time"),  # 普通复合索引, ser_cre是索引名
    # )
    # 联合索引/唯一索引，元组结构
    # __table_args__ = (
    #     UniqueConstraint('name', 'age', name='name_age'),  # 姓名和年龄唯一, name是索引名
    # )


if __name__ == '__main__':
    from hy_sqlite3.SQL import *

    # sqlite3数据库地址
    db = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path="test.db")
    # sqlalchemy的引擎, echo=False不打印执行的SQL语句
    engine = create_engine(db, echo=False)
    # 会话类绑定引擎
    Session = sessionmaker(bind=engine)
    # 开启会话实例
    session = Session()
    # 查询表， 没有就创建表
    tables = list(session.execute(sqlite3_001))
    if not tables:
        Models.metadata.create_all(engine)
    Models.metadata.create_all(engine)
    session.query(User).delete()
    session.query(Student).delete()
    session.query(Class).delete()
    session.query(ClassStudent).delete()
    """测试区"""
    # 插入数据
    try:
        user1 = User(username="student1")
        session.add(user1)
        user2 = User(username="student2")
        session.add(user2)
        # raise FileNotFoundError
        user1_1 = session.query(User).filter(User.username == 'student1').first()
        article1 = Article(title="title1", content="content1", author_id=user1_1.id)
        session.add(article1)
        session.commit()
    except Exception as err:
        session.rollback()

    s1 = Student(id=1, name="王鑫1")
    s2 = Student(id=2, name="王鑫仪2")
    c1 = Class(id=1, name="level1")
    c2 = Class(id=2, name="level2")
    # yyh 对于sqlalchemy下orm的夺标数据插入，必须插入多对多数据时，必须对例如：id，要某先指定id或者从数据库中查出的id
    cs1 = ClassStudent(class_id=c1.id, student_id=s1.id)
    cs2 = ClassStudent(class_id=c1.id, student_id=s2.id)
    cs3 = ClassStudent(class_id=c2.id, student_id=s1.id)
    cs4 = ClassStudent(class_id=c2.id, student_id=s2.id)

    session.add_all([s1, s2, c1, c2])
    session.add_all([cs1, cs2, cs3, cs4])
    session.commit()

    st1 = session.query(Student).filter_by(id=1).first()
    print(st1.name, st1.classes, [i.name for i in st1.classes])
    cl1 = session.query(Class).filter_by(id=1).first()
    print(cl1.name, cl1.students, [i.name for i in cl1.students])

    # 由于主键设置自动增长，不能重复
    try:
        u1 = User(id=3, username="q1")
        a1 = Article(id=3, title="title", content="content", author_id=u1.id)
        # a2 = Article(id=3, title="title", content="content", author_id=u1.id)
        session.add_all([u1, a1])
        session.commit()
    except Exception as err:
        session.rollback()

    # 正向查询
    article = session.query(Article).filter_by(id=1).first()
    print('文章标题：', article.title)
    print('该文章的id：', article.author_id)
    print('该文章的作者：', article.author)

    # 反向查询
    user = session.query(User).filter_by(id=1).first()
    print('username:', user.username)
    print('该作者对应的文章：', [(i.id, i.title) for i in user.articles])

    """"""
    # 提交至数据库
    session.commit()
    # 关闭会话
    session.close()
