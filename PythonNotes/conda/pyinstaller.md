### 使用

`pip install pyinstaller`

- 打包后的`exe`运行环境路径

```python
def resource_path(relative_path):
	"""exe在运行环境下的临时路径"""
	if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    path = os.path.join(base_path, relative_path)
    return path
```

- 命令行使用

```txt
-F	pyinstaller -F demo.py	只在dist中生产一个demo.exe文件。
-D	pyinstaller -D demo.py	默认选项，除了demo.exe外，还会在在dist中生成很多依赖文件，推荐使用。
-c	pyinstaller -c demo.py	默认选项，只对windows有效，使用控制台，就像编译运行C程序后的黑色弹窗。
-w	pyinstaller -w demo.py	只对windows有效，不使用控制台。
-p	pyinstaller -p E:\python\Lib\site-packages demo.py	设置导入路径，一般用不到。
-i	pyinstaller -i D:\file.icon demo.py	将file.icon设置为exe文件的图标，推荐一个icon网站:https://tool.lu/tinyimage/

```

- 将资源文件一起打包

```shell
python35\Scripts\pyinstaller.exe -F P2.py --add-data="D:\WORKSPACE\Company_Projects\DesenseOtaReport\TD\Montserrat.ttf;."
# 其中第二个参数可以用.代表用户的临时路径(C:\Users\用户名\AppData\Local\Temp\临时文件夹\);

# 在.spec文件中的 datas=[("fonts\\Montserrat.ttf","./fonts/")],
# ./fonts/代表资源会释放在临时路径Temp/临时文件夹/fonts的路径下;
# 调用时可以以./fonts/为前缀获取资源绝对路径，访问当前临时路径文件夹下fonts下的的资源
```

