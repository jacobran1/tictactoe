import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit


class Ui_MainWindow(object):
    def __init__(self):
        self.current_move = "x"
        self.field_1_status = ""
        self.field_2_status = ""
        self.field_3_status = ""
        self.field_4_status = ""
        self.field_5_status = ""
        self.field_6_status = ""
        self.field_7_status = ""
        self.field_8_status = ""
        self.field_9_status = ""


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Крестики-нолики")
        MainWindow.resize(421, 499)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.choose_name_1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.choose_name_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.field_1 = QtWidgets.QPushButton(self.centralwidget)
        self.field_1.setGeometry(QtCore.QRect(60, 100, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(64)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.field_1.setFont(font)
        self.field_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_1.setText("")
        self.field_1.setObjectName("field_1")
        self.field_1.clicked.connect(self.def_field_1)
        self.field_2 = QtWidgets.QPushButton(self.centralwidget)
        self.field_2.setGeometry(QtCore.QRect(160, 100, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_2.setFont(font)
        self.field_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_2.setText("")
        self.field_2.setObjectName("field_2")
        self.field_2.clicked.connect(self.def_field_2)
        self.field_3 = QtWidgets.QPushButton(self.centralwidget)
        self.field_3.setGeometry(QtCore.QRect(260, 100, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_3.setFont(font)
        self.field_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_3.setText("")
        self.field_3.setObjectName("field_3")
        self.field_3.clicked.connect(self.def_field_3)
        self.field_4 = QtWidgets.QPushButton(self.centralwidget)
        self.field_4.setGeometry(QtCore.QRect(60, 190, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_4.setFont(font)
        self.field_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_4.setText("")
        self.field_4.setObjectName("field_4")
        self.field_4.clicked.connect(self.def_field_4)
        self.field_5 = QtWidgets.QPushButton(self.centralwidget)
        self.field_5.setGeometry(QtCore.QRect(160, 190, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_5.setFont(font)
        self.field_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_5.setText("")
        self.field_5.setObjectName("field_5")
        self.field_5.clicked.connect(self.def_field_5)
        self.field_6 = QtWidgets.QPushButton(self.centralwidget)
        self.field_6.setGeometry(QtCore.QRect(260, 190, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_6.setFont(font)
        self.field_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_6.setText("")
        self.field_6.setObjectName("field_6")
        self.field_6.clicked.connect(self.def_field_6)
        self.field_7 = QtWidgets.QPushButton(self.centralwidget)
        self.field_7.setGeometry(QtCore.QRect(60, 280, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_7.setFont(font)
        self.field_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_7.setText("")
        self.field_7.setObjectName("field_7")
        self.field_7.clicked.connect(self.def_field_7)
        self.field_8 = QtWidgets.QPushButton(self.centralwidget)
        self.field_8.setGeometry(QtCore.QRect(160, 280, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_8.setFont(font)
        self.field_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_8.setText("")
        self.field_8.setObjectName("field_8")
        self.field_8.clicked.connect(self.def_field_8)
        self.field_9 = QtWidgets.QPushButton(self.centralwidget)
        self.field_9.setGeometry(QtCore.QRect(260, 280, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.field_9.setFont(font)
        self.field_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.field_9.setText("")
        self.field_9.setObjectName("field_9")
        self.field_9.clicked.connect(self.def_field_9)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(250, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
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
        self.label.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "-Игрок1"))
        self.label_2.setText(_translate("MainWindow", "O"))
        self.pushButton_2.setText(_translate("MainWindow", "-Игрок2"))
        self.label_3.setText(_translate("MainWindow", "Счёт:    n : m"))
        self.pushButton_12.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_13.setText(_translate("MainWindow", "Выйти"))

    def check(self):
        self.field_1.setText(self.field_1_status.upper())
        self.field_2.setText(self.field_2_status.upper())
        self.field_3.setText(self.field_3_status.upper())
        self.field_4.setText(self.field_4_status.upper())
        self.field_5.setText(self.field_5_status.upper())
        self.field_6.setText(self.field_6_status.upper())
        self.field_7.setText(self.field_7_status.upper())
        self.field_8.setText(self.field_8_status.upper())
        self.field_9.setText(self.field_9_status.upper())

    def choose_name_1(self):
        text, pressed = QInputDialog.getText(window, "", "Введите имя первого игрока: ",
                                             QLineEdit.Normal, "")
        if pressed:
            self.pushButton.setText(f"-{text}")

    def choose_name_2(self):
        text, pressed = QInputDialog.getText(window, "", "Введите имя второго игрока: ",
                                             QLineEdit.Normal, "")
        if pressed:
            self.pushButton_2.setText(f"-{text}")

    def def_field_1(self):
        if self.current_move == "x":
            self.field_1_status = "x"
            self.current_move = "o"
        else:
            self.field_1_status = "o"
            self.current_move = "x"
        self.field_1.setEnabled(False)
        self.field_1.setStyleSheet("color: black;")
        self.check()

    def def_field_2(self):
        if self.current_move == "x":
            self.field_2_status = "x"
            self.current_move = "o"
        else:
            self.field_2_status = "o"
            self.current_move = "x"
        self.field_2.setEnabled(False)
        self.field_2.setStyleSheet("color: black;")
        self.check()


    def def_field_3(self):
        if self.current_move == "x":
            self.field_3_status = "x"
            self.current_move = "o"
        else:
            self.field_3_status = "o"
            self.current_move = "x"
        self.field_3.setEnabled(False)
        self.field_3.setStyleSheet("color: black;")
        self.check()


    def def_field_4(self):
        if self.current_move == "x":
            self.field_4_status = "x"
            self.current_move = "o"
        else:
            self.field_4_status = "o"
            self.current_move = "x"
        self.field_4.setEnabled(False)
        self.field_4.setStyleSheet("color: black;")
        self.check()


    def def_field_5(self):
        if self.current_move == "x":
            self.field_5_status = "x"
            self.current_move = "o"
        else:
            self.field_5_status = "o"
            self.current_move = "x"
        self.field_5.setEnabled(False)
        self.field_5.setStyleSheet("color: black;")
        self.check()


    def def_field_6(self):
        if self.current_move == "x":
            self.field_6_status = "x"
            self.current_move = "o"
        else:
            self.field_6_status = "o"
            self.current_move = "x"
        self.field_6.setEnabled(False)
        self.field_6.setStyleSheet("color: black;")
        self.check()


    def def_field_7(self):
        if self.current_move == "x":
            self.field_7_status = "x"
            self.current_move = "o"
        else:
            self.field_7_status = "o"
            self.current_move = "x"
        self.field_7.setEnabled(False)
        self.field_7.setStyleSheet("color: black;")
        self.check()


    def def_field_8(self):
        if self.current_move == "x":
            self.field_8_status = "x"
            self.current_move = "o"
        else:
            self.field_8_status = "o"
            self.current_move = "x"
        self.field_8.setEnabled(False)
        self.field_8.setStyleSheet("color: black;")
        self.check()


    def def_field_9(self):
        if self.current_move == "x":
            self.field_9_status = "x"
            self.current_move = "o"
        else:
            self.field_9_status = "o"
            self.current_move = "x"
        self.field_9.setEnabled(False)
        self.field_9.setStyleSheet("color: black;")
        self.check()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())