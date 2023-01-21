from PyQt5.QtWidgets import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,400)
        self.text = QLabel("birinchi oyna",self)
        self.btn = QPushButton("Click",self)
        self.btn.move(150,50)
        self.btn.clicked.connect(self.opensecond)

    def opensecond(self):
        self.secondwin = secondwindow()
        self.secondwin.show()
        self.close()

class secondwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,400)
        self.text = QLabel("birinchi oyna",self)
        self.btn = QPushButton("Click",self)
        self.btn.move(150,50)
        self.btn.clicked.connect(self.openfirst)

    def openfirst(self):
        self.firstwin = MainWindow()
        self.firstwin.show()
        self.close()

app = QApplication(sys.argv)
window = MainWindow
window.show()
app.exec_()
