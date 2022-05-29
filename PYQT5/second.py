#pip install PyQt5
#pip install pyqt5-tools
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow
from PyQt5.QtGui import QIcon
class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()#why used super class
        self.setGeometry(600,300,600,400)
        self.setWindowTitle("My title")
        self.setWindowIcon(QIcon("my.png"))
        #self.setWindowOpacity(0.5)
        self.setStyleSheet('background-color:red')



app = QApplication(sys.argv)

window = mywindow()

window.show()

app.exec_() # app exit wind
