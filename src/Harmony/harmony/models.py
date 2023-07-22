from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum
# from sqlalchemy import Enum
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class PollEnum(enum.Enum):
    POLL_ARTICLE = 1
    POLL_COMMIT = 2
    POLL_USER = 0


class GenderEnum(enum.Enum):
    male = 1
    female = 0
    secret = -1


class BaseModel(object):
    create_time = db.Column(db.Integer, default=datetime.utcnow)
    update_time = db.Column(db.Integer, default=datetime.utcnow)
    isDelete = db.Column(db.Boolean, default=False)


# 收集关系表
class UserArticle(db.Model):
    __tablename__ = 'tb_user_article'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article_info.id'))
    db.UniqueConstraint('user_id', 'article_id', name='collect_relation')


# 关注关系表
tb_user_user = db.Table(
    'tb_user_user',
    # 在多个字段上设置primary_key=True，表示设置联合主键，这几个列的值全到一起，作主键
    db.Column('follower_id', db.Integer, db.ForeignKey('user_info.id'), primary_key=True),
    db.Column('followee_id', db.Integer, db.ForeignKey('user_info.id'), primary_key=True),
    db.UniqueConstraint('follower_id', 'followee_id', name='follow_relation')
)


class User(db.Model, BaseModel):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    signature = db.Column(db.String(200), default='')
    qq_openid = db.Column(db.String(255))
    wx_openid = db.Column(db.String(255))
    github_openid = db.Column(db.String(255))
    password_hash = db.Column(db.String(200))
    mobile = db.Column(db.String(11))
    avatar = db.Column(db.String(50), default='user_pic.png')
    # 关注
    follow_count = db.Column(db.Integer, default=0)
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.secret)
    isAdmin = db.Column(db.Boolean, default=False)
    articles = db.relationship('Article', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    hot_key_category = db.relationship('HotKeyCategory', backref='user', lazy='dynamic')
    article_collect = db.relationship('Article', secondary='UserArticle', lazy='dynamic', backref='user')  # 多对多关系

    # 自关联的多对多关系
    # user.follower 用户关注的对象
    # user.followee 用户粉丝的对象
    followers = db.relationship(
        'User',
        secondary=tb_user_user,  # 通过secondary指定多对多的外键关系表
        lazy='dynamic',  # 设置lazy='dynamic', 表示在查询某一个user时， 是否会查询该用户, 其关注的对象
        primaryjoin=id == tb_user_user.c.follower_id,  # 主要关联条件，从子对象查询其父对象
        secondaryjoin=id == tb_user_user.c.followee_id,  # 辅助关联条件，从父对象查询其所有子对象
        backref=db.backref('followee', lazy='dynamic')  # 反向引用
    )

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def check_pwd(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}


class Poll(db.Model, BaseModel):
    __tablename__ = 'poll_info'
    id = db.Column(db.Integer, primary_key=True)
    poll_type = db.Column(db.Enum(PollEnum), default=PollEnum.POLL_ARTICLE)
    article_id = db.Column(db.Integer, db.ForeignKey('article_info.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment_info.id'))

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}


class Article(db.Model, BaseModel):
    __tablename__ = 'article_info'
    id = db.Column(db.Integer, primary_key=True)
    # 作者
    author_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    # 标题
    title = db.Column(db.String(32))
    # 摘要
    summary = db.Column(db.String(128))
    # 文章主题
    context = db.Column(db.Text)
    # 评论数
    comment_count = db.Column(db.Integer, default=0)
    # 阅读数
    read_count = db.Column(db.Integer, default=0)
    # 点赞数
    poll_count = db.Column(db.Integer, default=0)
    # 评论查询关系
    comments = db.relationship('Comment', backref='article', lazy='dynamic', order_by='Comment.id.desc()')

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}


class Comment(db.Model, BaseModel):
    __tablename__ = 'comment_info'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article_info.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))
    poll_count = db.Column(db.Integer, default=0)
    msg = db.Column(db.String(255))
    # 自关联
    comment_id = db.Column(db.Integer, db.ForeignKey('comment_info.id'))
    comments = db.relationship('Comment', backref='comment_up', lazy='dynamic')

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}


class HotKey(db.Model, BaseModel):
    __tablename__ = 'hot_key_info'
    id = db.Column(db.Integer, primary_key=True)
    key_group = db.Column(db.String(32))
    msg = db.Column(db.String(255))
    category = db.Column(db.ForeignKey('hot_key_category_info.id'))

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}


class HotKeyCategory(db.Model, BaseModel):
    __tablename__ = 'hot_key_category_info'
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(255))
    hot_keys = db.relationship('HotKey', backref='hot_key_category', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    def __repr__(self):
        return "<%(cls)s %(id)s>" % {"cls": self.__class__.__name__, "id": self.id}
