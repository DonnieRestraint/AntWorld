import functools
from random import random
import re
from flask import Blueprint, request, jsonify, session, make_response, current_app, redirect, g, render_template
from datetime import datetime

from harmony.models import db, User
from harmony.utils.captcha import *
from harmony.view import *

user_blueprint = Blueprint('user', __name__, url_prefix='/user')


@user_blueprint.route('/image_code')
def image_code():
    # 获取第三方验证码生成模块
    name, text, image = captcha.generate_captcha()
    session["image_code"] = text

    # 创建图片响应
    response = make_response(image)
    response.mimetype = 'image/png'
    return response


@user_blueprint.route('/sms_code')
def sms_code():
    mobile = request.args.get("mobile")
    image_code_request = request.args.get('image_code')
    agree = request.form.get('agree')
    if not agree:
        return jsonify(get_jsonify(2))
    if not all([mobile, image_code_request]):
        return jsonify(get_jsonify(4))
    if image_code_request != session.pop('image_code'):
        return jsonify(get_jsonify(3))
    sms_code_value = str(random.randint(123456, 987654))
    session['sms_code'] = sms_code_value
    # y
    return jsonify(get_jsonify(1))


@user_blueprint.route('/email_code')
def email_code():
    mobile = request.args.get("email")
    image_code_request = request.args.get('image_code')
    agree = request.form.get('agree')
    if not agree:
        # 协议未通过
        return jsonify(get_jsonify(2))
    if not all([mobile, image_code_request]):
        # 输入信息不合规
        return jsonify(get_jsonify(4))
    if image_code_request != session.pop('image_code'):
        # 验证失败
        return jsonify(get_jsonify(3))
    sms_code_value = str(random.randint(123456, 987654))
    session['email_code'] = sms_code_value
    # y
    return jsonify(get_jsonify(1))


@user_blueprint.route('/register_mobile', methods=['POST'])
def register_mobile():
    mobile = request.form.get('mobile')
    image_code_request = request.form.get('image_code')
    pwd = request.form.get('pwd')
    agree = request.form.get('agree')
    if not agree:
        # 协议未通过
        return jsonify(get_jsonify(2))
    sms_code_session = session.pop('email_code')
    if sms_code_session != image_code_request:
        # 验证失败
        return jsonify(get_jsonify(3))
    if len(pwd) < 6:
        # 密码长度不合规
        return jsonify(get_jsonify(4))
    mobile_exists = User.query.filter(mobile=mobile).count()
    if mobile_exists:
        # 已存在
        return jsonify(get_jsonify(5))
    user = User()
    user.username = mobile
    user.email = mobile
    user.password = pwd
    db.session.add(user)
    db.session.commit()
    # y
    return jsonify(get_jsonify(1))


@user_blueprint.route('/register_email', methods=['POST'])
def register_email():
    email = request.form.get('email')
    image_code_request = request.form.get('image_code')
    pwd = request.form.get('pwd')
    agree = request.form.get('agree')
    if not agree:
        # 协议未通过
        return jsonify(get_jsonify(2))
    sms_code_session = session.pop('email_code')
    if sms_code_session != image_code_request:
        # 验证失败
        return jsonify(get_jsonify(3))
    if len(pwd) < 6:
        # 密码长度不合规
        return jsonify(get_jsonify(4))
    email_exists = User.query.filter(email=email).count()
    if email_exists:
        # 已存在
        return jsonify(get_jsonify(5))
    user = User()
    user.username = email
    user.email = email
    user.password = pwd
    db.session.add(user)
    db.session.commit()
    # y
    return jsonify(get_jsonify(1))


@user_blueprint.route('/login', methods=['POST'])
def login():
    account = request.form.get('account')
    pwd = request.form.get('account')
    if not all([account, pwd]):
        # 输入信息不足
        return jsonify(get_jsonify(3))
    is_email = check_email(account)
    is_mobile = check_mobile(account)
    if is_email:
        user = User.query.filter_by(email=account).first()
    elif is_mobile:
        user = User.query.filter_by(mobile=account).first()
    else:
        # 第三方登录, qq, wx, github
        user = None
    if user:
        if user.check_pwd(pwd):
            current_time = datetime.now()
            user.update_time = current_time
            db.session.commit()
            hour_key = datetime.strftime(current_time, "%Y-%m-%d %H")
            hour = datetime.strftime(current_time, "%H")
            current_app.redis_client.hincrby(hour_key, hour, 1)
            session['user_id'] = user.id
            return jsonify(get_jsonify(1), avatar=user.avatar_url, username=user.username)
        else:
            # 密码错误
            return jsonify(get_jsonify(4))
    else:
        # 用户不存在
        return jsonify(get_jsonify(4))


@user_blueprint.route('/user_info', methods=['GET', 'POST'])
@required_login
def modify_user_info():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        user = User.query.get(session.get('user_id'))
        # 修改信息
        gender = request.form.get('gender')
        signature = request.form.get('signature')
        username = request.form.get('username')
        user.signature = signature
        user.username = username
        user.gender = gender
        db.session.commit()
        return jsonify(get_jsonify(1))


# @required_login
@user_blueprint.route('/')
def index():
    return jsonify({"Data": 200})
    # return render_template('200.html')
