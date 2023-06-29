# PIP

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

  

