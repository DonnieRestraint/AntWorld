### Python 开发环境配置Demo

- `conda`克隆已存在的环境

  ```
  # 克隆环境
  conda create -n new_env --clone exist_env
  # 删除环境
  conda remove -n your_env_name --all
  # 查看环境
  conda env list
  # 激活环境
  conda activate env_name
  # 退出环境
  conda deactivate
  ```

- `conda`下载安装第三方安装包, 指定环境 默认yes

  ```
  conda install 安装包 [-n env_name] [-y]
  ```

- `conda`配置文件路径：`C:\Users\用户名\.condarc`

  ```txt
  proxy_servers:
    http: http://账户:密码@ip:port
    https: http://账户:密码@ip:port
  
  show_channel_urls: true
  
  channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
    - defaults
  
  custom_channels:
    conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  report_errors: true
  ```

  

- `pip`下载安装第三方安装包

  ```
  pip install flask
  pip install flask-sqlalchemy
  pip install pymysql
  pip install tornado 
  pip install numpy
  pip install pandas
  pip install matplotlib
  pip install opencv-python
  pip install pillow
  pip install scipy
  pip install imageio
  pip install scikit-learn
  pip install tensorflow
  pip install pyyaml
  pip install configparser
  pip install scikit-image
  pip install PyQt5
  pip install pyqt5-tools
  pip install pyqtwebengine
  pip install pyqtchart
  ```

  

- `pip`配置文件路径：`C:\Users\用户名\AppData\Roaming\pip\pip.ini`

  ```
  [global]
  proxy=http://账户:密码@ip:port
  index-url=http://mirrors.aliyun.com/pypi/simple/
  disable-pip-version-check = true
  [install]
  trusted-host=mirrors.aliyun.com
  ```

  

- `requirements.txt`的生成

  ```shell
  # 生成requirements.txt
  pip freeze > requirements.txt 
  
  # 从requirements.txt安装依赖
  pip install -r requirements.txt 
  ```

  - 其中内容一般格式

  ```
  pyqtchart>=5.15.6
  pyqtchart==5.15.6
  ```

  

  

