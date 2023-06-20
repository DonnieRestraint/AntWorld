from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QradioButton功能测试')
window.resize(500, 500)

# 设置两组(男女，对错)互斥
red = QWidget(window)
red.setStyleSheet('background-color:red;')
red.move(50, 50)
red.resize(200, 200)

green = QWidget(window)
green.setStyleSheet('background:green;')
green.move(red.x() + red.width(), red.y() + red.height())
green.resize(200, 200)

rb_nan = QRadioButton('男-&Male', red)
rb_nan.move(70, 70)
rb_nan.setChecked(True)

rb_nv = QRadioButton('女-&Female', red)  # alt+F
rb_nv.move(70, 100)

rb_nv.setAutoExclusive(False)
rb_nan.setChecked(True)

rb_yes = QRadioButton('yes', green)
rb_yes.move(70, 70)

rb_no = QRadioButton('no', green)
rb_no.move(70, 100)

# 默认选中rb_yes
rb_yes.setChecked(True)

window.show()
sys.exit(app.exec_())
