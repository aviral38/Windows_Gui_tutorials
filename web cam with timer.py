# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import threading

s = 0
m = 0
h = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(490, 410, 281, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.l = QtWidgets.QLabel(self.centralwidget)
        self.l.setGeometry(QtCore.QRect(20, 20, 751, 311))
        self.l.setObjectName("l")
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(80, 450, 93, 28))
        self.b.setObjectName("b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.timer = QtCore.QTimer()
        self.b.clicked.connect(self.bb)
        self.timer.timeout.connect(self.Time)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l.setText(_translate("MainWindow", "TextLabel"))
        self.b.setText(_translate("MainWindow", "cam"))
    def bb(self):
        def a():
            cap=cv2.VideoCapture(0)
            count=0
            while True:
                ret,imge=cap.read()
                cv2.imwrite("frame%d.jpg"%count,imge)

                self.l.setPixmap(QtGui.QPixmap("frame%d.jpg"%count,imge))
                count+=1
                if count>2:
                    l=int(count)-2
                    os.remove("frame%d.jpg"%l)
                k=cv2.waitKey(30)&0xff
                if k==27:
                    break
            vidcap.release()
            cv2.destroyAllWindows()
        global s,m,h
        self.timer.start(1000)
        t1=threading.Thread(target=a)
        t1.start()
    def Time(self):
        global s,m,h

        if s < 59:
            s += 1
        else:
            if m < 59:
                s = 0
                m += 1
            elif m == 59 and h < 24:
                h += 1
                m = 0
                s = 0
            else:
                self.timer.stop()

        time = "{0}:{1}:{2}".format(h,m,s)

        self.lcdNumber.setDigitCount(len(time))
        self.lcdNumber.display(time)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
