from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8808, debug=True)
    """
    官方flask项目
    https://dormousehole.readthedocs.io/en/latest/tutorial/index.html
    项目可安装化
    https://dormousehole.readthedocs.io/en/latest/tutorial/install.html
    项目覆盖测试
    https://dormousehole.readthedocs.io/en/latest/tutorial/tests.html
    部署
    https://dormousehole.readthedocs.io/en/latest/tutorial/deploy.html
    继续开发
    https://dormousehole.readthedocs.io/en/latest/tutorial/next.html
    扩展
    https://dormousehole.readthedocs.io/en/latest/extensions.html#id3
    """