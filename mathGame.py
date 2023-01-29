from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QProgressBar, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer
import sys
import time
from utils import createRandomExercises

from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    progressCount = 100
    point = 0
    difficulty = 2
    nextStepCounts = [5,6,8,12,12,13,14,14,14,14,14]
    nextStepIndex = 0
    step = 5
    triesCount = 0
    answer = 0
    exercises = ""

    def __init__(self):
        super().__init__()
        self.setFixedSize(500,300)

        self.randomExercises = createRandomExercises(self.difficulty)
        self.checkExercises = self.randomExercises
        
        self.answer = self.randomExercises["answer"]
        self.exercises = self.randomExercises["exercises"]+"=?"
        self.label = QLabel(self.exercises,self)
        self.label.setStyleSheet("font-size:40px")

        self.mainUi()

    def mainUi(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkGameEnd)

        self.layout = QVBoxLayout()
        self.one = QPushButton("1",self)
        self.two = QPushButton("2",self)
        self.three = QPushButton("3",self)
        self.startGame = QPushButton('Start',self)
        self.one.setStyleSheet("font-size:30px")
        self.two.setStyleSheet("font-size:30px")
        self.three.setStyleSheet("font-size:30px")
        
        self.one.setEnabled(False)
        self.two.setEnabled(False)
        self.three.setEnabled(False)

        self.startGame.setStyleSheet("font-size:30px")
        
        self.progress = QProgressBar(self)
        self.progress.setValue(self.progressCount)
        self.progress.setTextVisible(False)


        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.one)
        self.layout.addWidget(self.two)
        self.layout.addWidget(self.three)
        self.layout.addWidget(self.startGame)
        self.setLayout(self.layout)

        self.startGame.clicked.connect(self.startNewGame)

        self.one.clicked.connect(self.oneButton)
        self.two.clicked.connect(self.twoButton)
        self.three.clicked.connect(self.threeButton)



    def oneButton(self):
        self.checkAnswer(1)

    def twoButton(self):
        self.checkAnswer(2)

    def threeButton(self):
        self.checkAnswer(3)

    def checkAnswer(self,answer):
        if(self.answer == answer):
            self.point = self.point + self.progressCount/20 * self.difficulty;
            self.triesCount += 1
            if(self.triesCount >= self.step):
                self.nextStepIndex += 1
                self.step = self.nextStepCounts[self.nextStepIndex]
                self.triesCount = 0
                self.difficulty += 1
            time.sleep(0.5)
            self.progressCount = 100
            self.progress.setValue(self.progressCount)
           
            newExercises = createRandomExercises(self.difficulty)
            if(newExercises == self.checkExercises):
                self.randomExercises = createRandomExercises(self.difficulty)
                self.checkExercises = self.randomExercises
            else:
                self.randomExercises = newExercises
            self.answer = self.randomExercises["answer"]
            self.exercises = self.randomExercises["exercises"]+"=?"
            self.label.setText(self.exercises)

            
        else:
            self.timer.stop()
            self.gameMessage()
            self.one.setEnabled(False)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.startGame.setText("Restart")





    def startNewGame(self):
        self.timer.start(20)
        self.startGame.setVisible(False)
        print(self.answer)
        
        self.one.setEnabled(True)
        self.two.setEnabled(True)
        self.three.setEnabled(True)



    def checkGameEnd(self):
        self.progressCount -= 1
        self.progress.setValue(self.progressCount)
        if(self.progressCount == 0):
            self.gameMessage()
    

    def gameMessage(self):
        msg = QMessageBox(self)
        msg.setText(f"Game over\nYour score: {self.point}")
        msg.setMinimumHeight(500)
        msg.exec_()
        self.startGame.setVisible(True)
        self.progressCount = 100
        self.progress.setValue(self.progressCount)
        self.point = 0
        self.step = self.nextStepCounts[0]
        self.nextStepIndex = 0
        self.triesCount = 0
        self.difficulty = 2
        self.randomExercises = createRandomExercises(self.difficulty)
        self.answer = self.randomExercises["answer"]
        self.exercises = self.randomExercises["exercises"]+"=?"
        self.label.setText(self.exercises)
        self.one.setEnabled(False)
        self.two.setEnabled(False)
        self.three.setEnabled(False)
        self.startGame.setText("Restart")

        self.timer.stop()


        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()