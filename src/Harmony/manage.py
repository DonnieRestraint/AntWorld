from harmony.config import config_dict
import harmony
from flask_script import Manager
from harmony.cac import CreateUser, CreateArticle, CreateLogin
from harmony.models import db
from flask_migrate import MigrateCommand, Migrate

# 获取flask环境
flask_app = harmony.create_app(config_dict["dev"])
# 迁移数据库
manager = Manager(flask_app)
Migrate(flask_app, db)
# 添加迁移命令db
manager.add_command('db', MigrateCommand)
# from flask_script import Server
# manager.add_command("runserver", Server())

# 扩展管理员创建等其他的命令
manager.add_command('createuser', CreateUser())
manager.add_command('createlogin', CreateLogin())
manager.add_command('createarticle', CreateArticle())

if __name__ == '__main__':
    # flask_script==2.0.6中__init__.py的_compat要使用相对引用

    manager.run()
"""
- 网站运行
python manage.py runserver
- 数据库迁移
运行指令 创建数据表
python manage.py db init
运行指令 提交修改
python manage.py db migrate
运行指令 执行修改
python manage.py db upgrade
"""
