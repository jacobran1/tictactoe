import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QLineEdit


class Ui_MainWindow(object):
    def __init__(self):
        self.counter = [0, 0]
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
        self.is_pressed_before_1 = False
        self.is_pressed_before_2 = False
        self.is_pressed_before_3 = False
        self.is_pressed_before_4 = False
        self.is_pressed_before_5 = False
        self.is_pressed_before_6 = False
        self.is_pressed_before_7 = False
        self.is_pressed_before_8 = False
        self.is_pressed_before_9 = False

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
        self.res = QtWidgets.QPushButton(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(60, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.res.setFont(font)
        self.res.setObjectName("res")
        self.res.clicked.connect(self.reset)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(250, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.exit_btn)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Крестики-нолики"))
        self.label.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "-Игрок 1"))
        self.label_2.setText(_translate("MainWindow", "O"))
        self.pushButton_2.setText(_translate("MainWindow", "-Игрок 2"))
        self.label_3.setText(_translate("MainWindow", "Счёт:    0 : 0"))
        self.res.setText(_translate("MainWindow", "Сбросить"))
        self.quit.setText(_translate("MainWindow", "Выйти"))

    def exit_btn(self):
        sys.exit(app.exec_())

    def reset(self):
        self.field_1.setText("")
        self.field_2.setText("")
        self.field_3.setText("")
        self.field_4.setText("")
        self.field_5.setText("")
        self.field_6.setText("")
        self.field_7.setText("")
        self.field_8.setText("")
        self.field_9.setText("")
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
        self.is_pressed_before_1 = False
        self.is_pressed_before_2 = False
        self.is_pressed_before_3 = False
        self.is_pressed_before_4 = False
        self.is_pressed_before_5 = False
        self.is_pressed_before_6 = False
        self.is_pressed_before_7 = False
        self.is_pressed_before_8 = False
        self.is_pressed_before_9 = False

    def wino(self):
        self.counter[1] += 1
        self.label_3.setText(f"Счёт:    {self.counter[0]} : {self.counter[1]}")
        self.reset()

    def win(self):
        self.counter[0] += 1
        self.label_3.setText(f"Счёт:    {self.counter[0]} : {self.counter[1]}")
        self.reset()

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
        if self.field_1_status == "x" and self.field_2_status == "x" and self.field_3_status == "x":
            self.win()
        if self.field_4_status == "x" and self.field_5_status == "x" and self.field_6_status == "x":
            self.win()
        if self.field_7_status == "x" and self.field_8_status == "x" and self.field_9_status == "x":
            self.win()
        if self.field_1_status == "x" and self.field_4_status == "x" and self.field_7_status == "x":
            self.win()
        if self.field_2_status == "x" and self.field_5_status == "x" and self.field_8_status == "x":
            self.win()
        if self.field_3_status == "x" and self.field_6_status == "x" and self.field_9_status == "x":
            self.win()
        if self.field_1_status == "x" and self.field_5_status == "x" and self.field_9_status == "x":
            self.win()
        if self.field_3_status == "x" and self.field_5_status == "x" and self.field_7_status == "x":
            self.win()

        if self.field_1_status == "o" and self.field_2_status == "o" and self.field_3_status == "o":
            self.wino()
        if self.field_4_status == "o" and self.field_5_status == "o" and self.field_6_status == "o":
            self.wino()
        if self.field_7_status == "o" and self.field_8_status == "o" and self.field_9_status == "o":
            self.wino()
        if self.field_1_status == "o" and self.field_4_status == "o" and self.field_7_status == "o":
            self.wino()
        if self.field_2_status == "o" and self.field_5_status == "o" and self.field_8_status == "o":
            self.wino()
        if self.field_3_status == "o" and self.field_6_status == "o" and self.field_9_status == "o":
            self.wino()
        if self.field_1_status == "o" and self.field_5_status == "o" and self.field_9_status == "o":
            self.wino()
        if self.field_3_status == "o" and self.field_5_status == "o" and self.field_7_status == "o":
            self.wino()

        if self.field_1_status != "" and self.field_2_status != "" and self.field_3_status != "" and \
                self.field_4_status != "" and self.field_5_status != "" and self.field_6_status != "" and \
                self.field_7_status != "" and self.field_8_status != "" and self.field_9_status != "":
            self.reset()

    def choose_name_1(self):
        text, pressed = QInputDialog.getText(window, "Крестики-нолики", "Введите имя первого игрока: ",
                                             QLineEdit.Normal, "")
        if pressed:
            self.pushButton.setText(f"-{text}")

    def choose_name_2(self):
        text, pressed = QInputDialog.getText(window, "Крестики-нолики", "Введите имя второго игрока: ",
                                             QLineEdit.Normal, "")
        if pressed:
            self.pushButton_2.setText(f"-{text}")

    def def_field_1(self):
        if self.is_pressed_before_1 is False:
            if self.current_move == "x":
                self.field_1_status = "x"
                self.current_move = "o"
            else:
                self.field_1_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_1 = True
        else:
            pass

    def def_field_2(self):
        if self.is_pressed_before_2 is False:
            if self.current_move == "x":
                self.field_2_status = "x"
                self.current_move = "o"
            else:
                self.field_2_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_2 = True
        else:
            pass

    def def_field_3(self):
        if self.is_pressed_before_3 is False:
            if self.current_move == "x":
                self.field_3_status = "x"
                self.current_move = "o"
            else:
                self.field_3_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_3 = True
        else:
            pass

    def def_field_4(self):
        if self.is_pressed_before_4 is False:
            if self.current_move == "x":
                self.field_4_status = "x"
                self.current_move = "o"
            else:
                self.field_4_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_4 = True
        else:
            pass

    def def_field_5(self):
        if self.is_pressed_before_5 is False:
            if self.current_move == "x":
                self.field_5_status = "x"
                self.current_move = "o"
            else:
                self.field_5_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_5 = True
        else:
            pass

    def def_field_6(self):
        if self.is_pressed_before_6 is False:
            if self.current_move == "x":
                self.field_6_status = "x"
                self.current_move = "o"
            else:
                self.field_6_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_6 = True
        else:
            pass

    def def_field_7(self):
        if self.is_pressed_before_7 is False:
            if self.current_move == "x":
                self.field_7_status = "x"
                self.current_move = "o"
            else:
                self.field_7_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_7 = True
        else:
            pass

    def def_field_8(self):
        if self.is_pressed_before_8 is False:
            if self.current_move == "x":
                self.field_8_status = "x"
                self.current_move = "o"
            else:
                self.field_8_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_8 = True
        else:
            pass

    def def_field_9(self):
        if self.is_pressed_before_9 is False:
            if self.current_move == "x":
                self.field_9_status = "x"
                self.current_move = "o"
            else:
                self.field_9_status = "o"
                self.current_move = "x"
            self.check()
            self.is_pressed_before_9 = True
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
