#pip install PyQt5
#pip install pyqt5-tools
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon
# class for setting window successfull
class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()#why used super class
        self.setGeometry(600,300,400,400)
        self.setWindowTitle("My title")
        self.setWindowIcon(QIcon("my.png"))
        #self.setStyleSheet('color:red')
        #self.setStyleSheet('background-color:red')
        #self.setWindowOpacity(0.5)
        #self.setStyleSheet('background-color:red')
        self.create_button()# calling button

    def create_button(self):
        btn1 = QPushButton("Click one",self)
        btn1.setGeometry(100,100,100,100)
        btn1.setIcon(QIcon("btn1.jpg"))
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:red')
        btn2 = QPushButton("Click two", self)
        btn2.setGeometry(200,100,100,100)
        btn2.setIcon(QIcon("btn2.png"))
        btn2.setStyleSheet('color:yellow')
        btn2.setStyleSheet('background-color:green')

app = QApplication(sys.argv)

window = mywindow()

window.show()

app.exec_() # app exit wind
