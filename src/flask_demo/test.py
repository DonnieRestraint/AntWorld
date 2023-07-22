import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from skimage import io
import imageio
import tensorflow as tf
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


class MyMiddleWare(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        print('开始之前')
        response = self.old_wsgi_app(environ, start_response)
        print('结束之后')
        return response


if __name__ == '__main__':
    # 把原来的wsgi_app替换为自定义的
    app.wsgi_app = MyMiddleWare(app.wsgi_app)
    app.run(host="0.0.0.0", port=8208, debug=True)