"""

"""

import cgitb
import sys
from PyQt5.QtWidgets import QApplication
from MoonLight.MainWidget import MainFrame
from MoonLight.StyleLoader import DEBUG

if __name__ == '__main__':
    cgitb.enable(format='text') if DEBUG else ...
    app = QApplication(sys.argv)
    frame = MainFrame()
    frame.show()
    sys.exit(app.exec())
