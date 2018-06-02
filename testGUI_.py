import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        button_1 = QPushButton("OKAY", self)
        button_1.move(100,100)
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("TEST GUI")
        self.show()


app=QApplication(sys.argv)
window = Fenster()
sys.exit(app.exec_())