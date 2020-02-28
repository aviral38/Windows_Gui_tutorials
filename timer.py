# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lr = QtWidgets.QLabel(self.centralwidget)
        self.lr.setGeometry(QtCore.QRect(510, 350, 211, 171))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lr.setFont(font)
        self.lr.setText("")
        self.lr.setObjectName("lr")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(20, 220, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(190, 220, 93, 101))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro Bold")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(20, 340, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(350, 337, 93, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(20, 460, 93, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(180, 460, 93, 101))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(360, 460, 93, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(350, 210, 93, 111))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(190, 350, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(470, 210, 93, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setObjectName("b0")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 40, 491, 131))
        self.lcdNumber.setObjectName("lcdNumber")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(620, 390, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(610, 260, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(630, 30, 111, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(630, 100, 111, 41))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(630, 180, 111, 51))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.timer = QtCore.QTimer()
        self.start_time = 00
        self.lcdNumber.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
        self.timer.timeout.connect(self.updateLCD)
        self.b1.clicked.connect(self.b1p)
        self.b2.clicked.connect(self.b2p)
        self.b3.clicked.connect(self.b3p)
        self.b4.clicked.connect(self.b4p)
        self.b5.clicked.connect(self.b5p)
        self.b6.clicked.connect(self.b6p)
        self.b7.clicked.connect(self.b7p)
        self.b8.clicked.connect(self.b8p)
        self.b9.clicked.connect(self.b9p)
        self.b0.clicked.connect(self.b0p)
        self.start.clicked.connect(self.ss)
        self.stop.clicked.connect(self.mn)
        self.dt=0
        self.i=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "stop"))
    def b1p(self):
        self.lr.setText(self.lr.text()+"1")
    def b2p(self):
        self.lr.setText(self.lr.text()+"2")
    def b3p(self):
        self.lr.setText(self.lr.text()+"3")
    def b4p(self):
        self.lr.setText(self.lr.text()+"4")
    def b5p(self):
        self.lr.setText(self.lr.text()+"5")
    def b6p(self):
        self.lr.setText(self.lr.text()+"6")
    def b7p(self):
        self.lr.setText(self.lr.text()+"7")
    def b8p(self):
        self.lr.setText(self.lr.text()+"8")
    def b9p(self):
        self.lr.setText(self.lr.text()+"9")
    def b0p(self):
        self.lr.setText(self.lr.text()+"0")
    def ss(self):
        self.x=int(self.lr.text())
        self.timer.stop()
        self.start_time = self.x
        self.lcdNumber.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
        self.timer.start(1000)
    def updateLCD(self):
        # Update the lcd
        self.start_time -= 1
        if self.start_time >= 0:
            self.lcdNumber.display("%d:%02d" % (self.start_time/60,self.start_time % 60))
        else:
            self.timer.stop()
    def mn(self):
        if self.dt==0:
            self.timer.stop()
            self.y=self.start_time
            self.dt=self.dt+1
            self.i=self.i+1
        elif self.dt%2==0:
            self.timer.stop()
            if(self.dt==2):
                self.z=self.start_time
            if(self.dt==4):
                self.fg=self.start_time
            self.dt=self.dt+1
        else:
            self.timer.start()
            self.k=self.x-self.y
            self.lcdNumber_2.display("%d:%02d" % (self.k/60,self.k % 60))
            if(self.dt==3):
                self.gh=self.y-self.z
                self.lcdNumber_3.display("%d:%02d" % (self.gh/60,self.gh % 60))
            if(self.dt==5):
                self.mm=self.z-self.fg
                self.lcdNumber_4.display("%d:%02d" % (self.mm/60,self.mm % 60))

            self.dt=self.dt+1
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
