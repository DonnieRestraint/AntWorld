

- ```shell
  # 安装环境管理器
  https://www.anaconda.com
  ```

- ```shell
  # 下载安装 CUDA(Compute Unified Device Architecture)，是一种新的操作GPU计算的硬件和软件架构
  https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local
  ```

- ```shell
  conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
  ```

- ```shell
  # 查询conda版本
  conda --version
  # 查询nvcc版本
  nvcc -V
  ```

- ```shell
  # 创建python环境
  conda create -n pytorch_env python=3.9
  activate pytorch_env
  
  conda deactivate
  ```

- ```shell
  pytorch官网 https://pytorch.org/
  # 使用官网安装
  conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
  
  更换镜像源后进行安装
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/win-64/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/win-64/
  conda config --set show_channel_urls yes
  conda config --set ssl_verify false
  # 使用更换的镜像源安装
  conda install pytorch torchvision cudatoolkit=11.3
  # 检查安装成功
  import torch
  print(torch.__version__)
  print('gpu:', torch.cuda.is_available())
  ```

