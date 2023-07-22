"""
CreateActionCommand
"""
from flask import current_app
import random
from flask_script.commands import Command
from harmony.models import User, db, Article, Comment, Poll


class CreateUser(Command):
    def run(self):
        # 提示输入用户名、密码
        username = input('请输入用户名：')
        password = input('请输入密码：')
        user = User()
        user.username = username
        user.password = password
        user.isAdmin = True
        db.session.add(user)
        # 提交
        db.session.commit()
        print("管理员创建成功")


class CreateLogin(Command):
    def run(self):
        for i in range(7, 23):
            current_app.redis_cli.hset('login2018-07-16', '%02d:00' % i, random.randint(20, 120))
        print('生成数据成功')


class CreateArticle(Command):
    def run(self):
        pass


class CreateComment(Command):
    def run(self):
        pass


class CreatePoll(Command):
    def run(self):
        pass
