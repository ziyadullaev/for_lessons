# from PyQt5.QtWidgets import QWidget,  QApplication, QLabel , QPushButton
# from PyQt5.QtCore import QTimer
# import sys
# import environs
# class Mainwindow(QWidget):
#     milliSec = 0
#     second = 0
#     minutes = 0
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(700,700)
#         self.label = QLabel('0',self)
#         self.label.setStyleSheet('font-size:80px;')
#         self.label.move(80,80)

#         self.btn = QPushButton('start',self)
#         self.btn.clicked.connect(self.startTimer)

#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.shownumbers)
#         self.timer.start(100)
    
#     def startTimer(self):
#         self.timer.start(100)

#     def shownumbers(self):
#         self.milliSec +=1
#         self.label.setText(str(self.milliSec/10))
#         self.label.adjustSize()
        
# app = QApplication(sys.argv)
# window = Mainwindow()
# window.show()
# app.exec_()

