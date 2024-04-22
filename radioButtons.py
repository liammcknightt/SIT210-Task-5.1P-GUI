import sys

import RPi.GPIO as GPIO

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

        def setupUi(self, MainWindow):   

                MainWindow.setObjectName("MainWindow")

                MainWindow.resize(389, 179)

                self.centralwidget = QtWidgets.QWidget(MainWindow)

                self.centralwidget.setObjectName("centralwidget")

                self.redButton = QtWidgets.QRadioButton(self.centralwidget)

                self.redButton.setGeometry(QtCore.QRect(60, 70, 82, 17))

                self.redButton.setObjectName("redButton")

                self.greenButton = QtWidgets.QRadioButton(self.centralwidget)

                self.greenButton.setGeometry(QtCore.QRect(170, 70, 82, 17))

                self.greenButton.setObjectName("greenButton")

                self.blueButton = QtWidgets.QRadioButton(self.centralwidget)

                self.blueButton.setGeometry(QtCore.QRect(290, 70, 82, 17))

                self.blueButton.setObjectName("blueButton")

                MainWindow.setCentralWidget(self.centralwidget)

                self.menubar = QtWidgets.QMenuBar(MainWindow)

                self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))

                self.menubar.setObjectName("menubar")

                MainWindow.setMenuBar(self.menubar)

                self.statusbar = QtWidgets.QStatusBar(MainWindow)

                self.statusbar.setObjectName("statusbar")

                MainWindow.setStatusBar(self.statusbar)



                self.retranslateUi(MainWindow)

                QtCore.QMetaObject.connectSlotsByName(MainWindow)



        def retranslateUi(self, MainWindow):

                _translate = QtCore.QCoreApplication.translate

                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

                self.redButton.setText(_translate("MainWindow", "Red"))

                self.greenButton.setText(_translate("MainWindow", "Green"))

                self.blueButton.setText(_translate("MainWindow", "Blue"))

                

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

        def __init__(self):

                super().__init__()

                self.setupUi(self)



                self.redLed = 9

                self.greenLed = 10

                self.blueLed = 11



                GPIO.setmode(GPIO.BCM)

                GPIO.setup(self.redLed, GPIO.OUT)

                GPIO.setup(self.greenLed, GPIO.OUT)

                GPIO.setup(self.blueLed, GPIO.OUT)



                self.redButton.toggled.connect(self.checkRedLed)

                self.greenButton.toggled.connect(self.checkGreenLed)

                self.blueButton.toggled.connect(self.checkBlueLed)



        def checkRedLed(self):

                if self.redButton.isChecked():

                        GPIO.output(self.redLed, GPIO.HIGH)

                        print("RED LED ON")

                else:

                        GPIO.output(self.redLed, GPIO.LOW)



        def checkGreenLed(self):

                if self.greenButton.isChecked():

                        GPIO.output(self.greenLed, GPIO.HIGH)

                        print("GREEN LED ON")

                else:

                        GPIO.output(self.greenLed, GPIO.LOW)



        def checkBlueLed(self):

                if self.blueButton.isChecked():

                        GPIO.output(self.blueLed, GPIO.HIGH)

                        print("BLUE LED ON")

                else:

                        GPIO.output(self.blueLed, GPIO.LOW)



        def closeEvent(self, event):

                GPIO.output(self.redLed, GPIO.LOW)

                GPIO.output(self.greenLed, GPIO.LOW)

                GPIO.output(self.blueLed, GPIO.LOW)

                GPIO.cleanup()



                super().closeEvent(event)



if __name__ == "__main__":

    GPIO.setwarnings(False)



    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    window.show()



    sys.exit(app.exec_())
