from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sys
import time

from PyQt5.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.mainVlayout = QVBoxLayout(self)
        self.inputField = QLineEdit(self)
        self.clearBtn = QPushButton('clear',self)
        self.clearBtn.setStyleSheet("font-size:18px")
        self.headerHlayout = QHBoxLayout(self)
        self.headerHlayout.addWidget(self.inputField)
        self.headerHlayout.addWidget(self.clearBtn)
        self.mainVlayout.addLayout(self.headerHlayout)
        self.numbersGrid = QGridLayout(self)

        self.nine = QPushButton('9',self)
        self.eight = QPushButton('8',self)
        self.seven = QPushButton('7',self)
        self.six = QPushButton('6',self)
        self.five = QPushButton('5',self)
        self.four = QPushButton('4',self)
        self.three = QPushButton('3',self)
        self.two = QPushButton('2',self)
        self.one = QPushButton('1',self)
        
        self.result = QPushButton('=',self)
        self.divide = QPushButton('/',self)
        self.zero = QPushButton('0',self)
        self.multiple = QPushButton('*',self)
        self.plus = QPushButton('+',self)
        self.minus = QPushButton('-',self)

        buttons = [self.nine,self.eight,self.seven,self.six,
                 self.five,self.four,self.three,self.two,self.one,
                self.result,self.divide,self.zero,self.multiple,
                 self.plus,self.minus
        ]

        stepCount = 0
        for i in range(5):
            for j in range(3):
                newBtn = buttons[stepCount]
                newBtn.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
                newBtn.setStyleSheet("font-size:18px")
                self.numbersGrid.addWidget(newBtn,i,j)
                stepCount += 1

        self.mainVlayout.addLayout(self.numbersGrid)

        self.setLayout(self.mainVlayout)



    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()