# Pyqt5



一、Pycharm设置向导Settings -> Tools -> External Tools -> +



二、在原生python环境下设置

```
在PyCharm设置Qt Designer
Program为: python安装目录下的\Lib\site-packages\pyqt5_tools\designer.exe
Working Directory为: $FileDir$

在PyCharm设置Pyuic
Program为: python安装目录下的\Scripts\pyuic5.exe
Arguments: $FileName$ -o $FileNameWithoutExtension$_qrc.py
Working Directory为: $FileDir$

在PyCharm设置Pyrcc5
Program为:python安装目录下的\Scripts\pyrcc5.bat
Arguments:$FileName$ -o $FileNameWithoutExtension$_qrc.py
Working Directory为:$FileDir$
```

在pyrcc5.exe同一目录下，新建一个带有以下一行代码的文件并命名为pyrcc5.bat, 与使用pyrcc5.exe效果一样，还可以避免一个未知问题

```shell
@"%~dp0\..\python" -m PyQt5.pyrcc_main %1 %2 %3 %4 %5 %6 %7 %8 %9
```



三、在Anaconda环境下设置：

```
Program:
D:\SOFTSPACE\Anaconda3\pkgs\pyqt-5.9.2-py39hd77b12b_6\Library\bin\pyrcc5.bat
D:\SOFTSPACE\Anaconda3\envs\gic\Scripts\pyuic5.exe
D:\SOFTSPACE\Anaconda3\Library\bin\designer.exe

Arguments: designer不需要参数
$FileName$ -o $FileNameWithoutExtension$_qrc.py

WorkDir: 三个都一样
$FileDir$

在命令行运行:
pyrcc5.bat :$FileName$ -o $FileNameWithoutExtension$_qrc.py
pyuic5.exe $FileName$ -o $FileNameWithoutExtension$_qrc.py
designer.exe
如： pyrcc5.exe img.qrc -o img_qrc.py
```



四、对于QRC资源的使用

在Pycharm中将`.qrc`文件中指定的资源以二进制形式储存于`.py`文件中

```xml
<RCC>
  <qresource prefix="/mf">
    <file alias="check">../images/checkbox-input.png</file>
    <file alias="uncheck">../images/uncheckbox-input.png</file>
    <file alias="close">../images/close.png</file>
    <file alias="minimize">../images/minimize.png</file>
    <file alias='maximize'>../images/Frame4.png</file>
  </qresource>
</RCC>
```

`<qresource>`标签中的prefix属性可有可无。
`<file>`标签中的文件路径是相对于当前`.qrc`文件的，应该在同一级目录或者`.qrc`文件所在目录的子目录，其`alias`属性还可以给文件完整路径取个别名。
访问上面添加的文件时，以`:/`或者`qrc:///`开始， 接着是`prefix`，后面是文件的alias属性值或者完整路径，如下例子所示：

```
:/images/checkbox-input.png
qrc:///mf/check
:/check
```

