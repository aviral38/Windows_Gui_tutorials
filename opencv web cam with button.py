# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ff.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import matplotlib.pyplot as plt
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(670, 455, 101, 101))
        self.l2.setText("")
        self.l2.setPixmap(QtGui.QPixmap("engg.jpg"))
        self.l2.setObjectName("l2")
        self.b = QtWidgets.QPushButton(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(120, 490, 93, 28))
        self.b.setObjectName("b")
        self.fr = QtWidgets.QFrame(self.centralwidget)
        self.fr.setGeometry(QtCore.QRect(120, 30, 621, 371))
        self.fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr.setObjectName("fr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.b.clicked.connect(self.j)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b.setText(_translate("MainWindow", "PushButton"))
    def j(self):
        self.cap = cv2.VideoCapture(0)
        while True:
            ret, self.frame=self.cap.read()
            cv2.imshow('frame',self.frame)
            if cv2.waitKey(1) & 0xFF== ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
