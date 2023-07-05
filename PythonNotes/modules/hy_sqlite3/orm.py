from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine, text
from sqlalchemy.orm import sessionmaker


class SqliteDb(object):
    debug = False
    echo = True if debug else False

    def __init__(self, db_path='test.db'):
        db = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path=db_path)
        self.engine = create_engine(db, echo=self.echo)
        # self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

    def with_session(*func_args):
        func = func_args[-1]

        def decorated(*args, **kwargs):
            self = args[0]
            session = self.get_session()
            kwargs["session"] = session
            try:

                f = func(*args, **kwargs)
                session.commit()
                session.close()
                return f
            except Exception as err:
                session.rollback()
                print(err)

        return decorated

    def create_table(self, table_name, *columns):
        meta = MetaData()
        table = Table(
            table_name,
            meta,
            *columns
        )
        meta.create_all(self.engine)
        return table

    def exe_sql(self, sql, args=None):
        with self.engine.connect() as con:
            try:
                # 'select * from persons'
                results = con.execute(sql, args)
                for result in results:
                    print(result)
            except Exception as err:
                print(err)

    @with_session
    def read(self, class_name, condition, **kwargs):
        session = kwargs.pop("session")
        # where = (class_name.name == 'ed') 和filter_by用法有些不同不能传递关键字参数
        result = session.query(class_name).filter(condition).first()
        keys = {}
        for k, v in result.__dict__.items():
            if k != "_sa_instance_state":
                keys[k] = v
        return class_name(**keys)

    @with_session
    def delete(self, class_name, **kwargs):
        session = kwargs.pop("session")
        del_user = session.query(class_name).filter_by(**kwargs).first()
        session.delete(del_user)

    @with_session
    def update(self, class_name, where, **kwargs):
        session = kwargs.pop("session")
        # where = (class_name.name == 'ed')
        result = session.query(class_name).filter(where).first()
        for key, val in kwargs.items():
            setattr(result, key, val)

    @with_session
    def create(self, *args, **kwargs):
        session = kwargs.pop("session")
        session.add_all(args)

    def get_session(self):
        return sessionmaker(bind=self.engine)()


if __name__ == '__main__':
    """
    Python3+SQLAlchemy+Sqlite3实现ORM教程：http://www.noobyard.com/article/p-ejbggzgx-c.html
    sqlalchemy ORM建表：https://blog.csdn.net/m0_57145438/article/details/130874157
    Mysql教程：http://c.biancheng.net/view/2580.html
    """

    from sqlalchemy.ext.declarative import declarative_base

    Models = declarative_base()


    class User(Models):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True, autoincrement=True)
        username = Column(String(100), nullable=False)


    sdb = SqliteDb()
    # 使用类中数据创建表
    Models.metadata.create_all(sdb.engine)
    # 使用组装的数据创建表
    sdb.create_table(User.__tablename__,
                     Column("id", Integer, primary_key=True, autoincrement=True),
                     Column("username", String(100), nullable=False)
                     )
    # ORM增查改删
    name = "神里"
    user = User(username=name)
    sdb.create(user)
    user_read = sdb.read(User, (User.username == name))
    sdb.update(User, (User.id == user_read.id), username="凌华")
    sdb.delete(User, id=user_read.id)

    # session
    from sqlalchemy import all_
    session = sdb.get_session()
    print(session.query(User).get(1).username)
    print(session.query(User).filter(all_(session.query(User.id).subquery())))
    print()
    # # 接近sql语法的ORM
    from sqlalchemy import insert, select, bindparam
    from hy_sqlite3.models import Article
    scalar_sub = select(User.id).where(User.username == bindparam('username')).scalar_subquery()
    with sdb.engine.connect() as conn:
        result = conn.execute(
            insert(Article).values(author_id=scalar_sub),
            [
                {"username": 'student1', "title": "title1", "content": "student1", "t": "1"},
                {"username": 'q1', "title": "title2", "content": "student2"},

            ]
        )

        print(insert(Article).returning(Article.id, Article.title))

        insert_stmt = insert(Article).from_select(
            ["title", "content", "author_id"],
            select(User.username, User.username, User.id)
        )
        # print(insert_stmt.returning(Article.title, Article.content, Article.author_id, ))
        conn.execute(insert_stmt)
    # 使用原生sql
    # with sdb.engine.connect() as conn:
    #     user_sql = text("select * from user")
    #     q_result = conn.execute(user_sql)
    #     for dict_row in q_result.mappings():
    #         x = dict_row['username']
    #         y = dict_row['id']
    #         print(x, y)

