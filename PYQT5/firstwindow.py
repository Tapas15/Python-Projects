#pip install PyQt5
#pip install pyqt5-tools

import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication(sys.argv)

win = QWidget()

win.show()

app.exec_() # app exit wind


import sys
from PyQt5.QtWidgets import QApplication,QWidget

app = QApplication([])

win = QWidget()

win.show()

app.exec_() # app exit wind
