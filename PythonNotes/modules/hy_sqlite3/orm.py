from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine
from sqlalchemy.orm import sessionmaker


class SqliteDb(object):
    debug = True
    echo = True if debug else False

    def __init__(self, db_path='test.db'):
        db = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path=db_path)
        self.engine = create_engine(db, echo=self.echo)

    def create_table(self, table_name, **kwargs):
        meta = MetaData()
        columns = [Column(str(field_name), field_type) for field_name, field_type in kwargs.items()]
        table = Table(
            table_name,
            meta,
            Column('id', Integer, primary_key=True),
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

    def read(self, class_name, condition):
        session = self.get_session()
        # where = (class_name.name == 'ed')
        results = session.query(class_name).filter(condition).first()
        return results

    def delete(self, table, **kwargs):
        session = self.get_session()
        try:
            del_user = session.query(table).filter_by(**kwargs).first()
            # 将ed用户记录删除
            session.delete(del_user)
            session.commit()
        except Exception as err:
            # session.rollback()
            print(err)

    def update(self, class_name, where, **kwargs):
        session = self.get_session()
        try:
            where = (class_name.name == 'ed')
            result = session.query(class_name).filter_by(where).first()
            for key, val in kwargs.items():
                setattr(result, key, val)
        except Exception as err:
            session.rollback()
            print(err)

    def create(self, *args):
        session = self.get_session()
        try:
            session.add_all(args)
            session.commit()
        except Exception as err:
            session.rollback()
            print(err)

    def get_session(self):
        return sessionmaker(bind=self.engine)()


if __name__ == '__main__':
    print("http://www.noobyard.com/article/p-ejbggzgx-c.html")
    print("https://blog.csdn.net/m0_57145438/article/details/130874157")
    print("https://blog.csdn.net/qq_41741971/article/details/126217235")

