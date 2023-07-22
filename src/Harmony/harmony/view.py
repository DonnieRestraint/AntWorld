from flask import session, redirect, g
import functools
import re
from harmony.models import User

statue_code = [
    (0, ""),
    (1, "Success"),
    (2, "Agreement not agreed"),
    (3, "Validation failed"),
    (4, "Operation failed"),
    (5, "Operation repetition"),
]


def required_login(view_fun):
    @functools.wraps(view_fun)
    def func(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/')
        user_id = session.get('user_id')
        # 绑定至单次响应对象
        g.user = User.query.get(user_id)
        return view_fun(*args, **kwargs)

    return func


def check_email(account):
    if re.match(r"^[+-]?\d+(.\d+)?$", account):
        return True
    else:
        return False


def check_mobile(account):
    if re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', account):
        return True
    else:
        return False


def get_jsonify(code):
    msg = dict(statue_code).get(code, None)
    if msg:
        return {code: msg}
    else:
        return {4, dict(statue_code).get(4)}
