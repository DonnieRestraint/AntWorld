import sqlalchemy
from sqlalchemy import MetaData, Integer, Column, Table, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

models = declarative_base()
class SqliteDb(object):
    debug = True
    echo = True if debug else False

    def __init__(self, db_path):
        self.sqlite_url = 'sqlite:///{db_path}?check_same_thread=False'.format(db_path="foo.db")
        self.engine = create_engine(self.sqlite_url, self.echo)
        self.Session = sessionmaker(bind=self.engine)

    def create_table(self, table_name, *args):
        meta = MetaData()
        Column('id', Integer, primary_key=True),
        columns = [Column(str(arg), String(32)) for arg in args]
        table = Table(
            table_name,
            meta,
            Column('id', Integer, primary_key=True),
            *columns
        )
        meta.create_all(self.engine)

    def delete(self, table, *args):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def create(self):
        pass