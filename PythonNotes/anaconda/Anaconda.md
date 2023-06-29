# Anaconda

### 下载

- https://www.anaconda.com/products/distribution

### 测试

- ```shell
  conda -V
  python -V
  ```

### 配置.condarc

配置样本

```txt
proxy_servers:
  http: http://用户名:密码@ip:port
  https: http://用户名:密码@ip:port

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
```

配置添加

```
conda config --set proxy_servers.http http://user:pwd@ip:port
conda config --set proxy_servers.https https://user:pwd@ip:port
conda config --set show_channel_urls yes	# 设置搜索时显示通道地址
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --remove channels defaults	# 刪除defaults
conda config --add channels defaults
```

### 更换镜像源

- [清华大学开源软件镜像站](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)

  ```shell
  # 添加清华源
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
   
  # 添加阿里云镜像源
  conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/free/
  conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main/
   
  # 添加中科大源
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
  ```

  


### conda使用

#### 默认在base环境下使用

```shell
# 创建虚拟python环境envName
conda create --name envName python=3.8
# 查看当前环境的安装文件包
conda list
# 查看指定环境的安装文件包
conda list -n envName
# 查看所有虚拟环境
conda env list
# 激活指定环境
conda activate envName
# 退出已激活的环境
conda deactivate
# 删除指定虚拟环境
conda remove -n envName --all
# 清理缓存
conda clean -all
# 克隆环境
conda create --name envName --clone old_envName
# 清除索引缓存, 目的是为了使用镜像源的索引
conda clean -i
# 批量安装第三方包
conda install --yes --file=requirements_conda.txt
pip install -r requirements_conda.txt
```

```shell
# 移植环境
# 1 移植conda安装的环境
conda activate envName
conda env export > envName.yaml
conda env create -f envName.yaml的绝对路径 -n envName
# 2 移植pip安装的环境
pip freeze > envName.txt
pip install -r envName.txt
```



#### 在激活环境后使用

````shell
# 安装xxx文件包：
conda install xxx
# 更新xxx文件包：
conda update xxx
# 卸载xxx文件包：
conda uninstall xxx
````



### pip配置

```
[global]
proxy=http://用户:密码@ip:port
index-url=http://mirrors.aliyun.com/pypi/simple/
disable-pip-version-check = true
[install]
trusted-host=mirrors.aliyun.com
```

本地环境安装,需要自己查看并安装依赖:

```
使用setup.py安装
	unzip numpy-1.13.1.zip
    cd numpu-1.13.1
    #指定安装路径
    python setup.py install --prefix=/path/to/install  # 等号后面写安装路径
使用whl格式文件安装
    pip install 123.whl # 123.whl 是whl包的名字
    #我们可以通过添加 --target=/path/to/install 来指定安装路径
```

