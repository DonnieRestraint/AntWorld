

### Git相关SSH配置

- windows10目前都是带有SSH，如果命令不对，请自行解决

- ```
  如果不存在， 可以先创建目录：`C:\Users\用户名\.ssh`
  ```

- ```
  ssh-keygen -t rsa -C xxxxxxxxx@xxx.com	# 生成id_rsa; id_rsa.pub
  输入文件名：id_rsa_github
  可以不输入密码：
  可以不输入密码：
  ```

- ```
  # github account
  Host github.com
  HostName github.com
  User 用户名
  IdentityFile C:\\Users\\用户名\\.ssh\\id_rsa_github
  IdentitiesOnly yes
  PreferredAuthentications publickey
  
  # gitlab account
  Host gitlab.com
  HostName gitlab.com
  User 用户名
  IdentityFile C:\\Users\\用户名\\.ssh\\id_rsa_gitlab
  IdentitiesOnly yes
  PreferredAuthentications publickey
  ```

- 
  
  ```
  # 以上是自己在.ssh下创建的文件config
  HostName:这个是真实的域名地址
  IdentityFile:这里是id_rsa的地址
  PreferredAuthentications:配置登录时用什么权限认证--可设为publickey,password等
  User:配置使用用户名
  ```
  
- ```
  点击个人头像
  点击Settings
  点击SSH and GPG keys
  点击New SSH key
  ```

- ```
  输入Title:任意名字
  输入key: 将id_rsa_github.pub的内容
  ```

- ```
  git clone 仓库地址
  ```

  
