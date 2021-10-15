import PyQt6.QtWidgets
from text_to_num import text2num
from spellchecker import SpellChecker
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(298, 286)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(5, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_error = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.gridLayout.addWidget(self.label_error, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_correction = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_correction.setFont(font)
        self.label_correction.setObjectName("label_correction")
        self.gridLayout.addWidget(self.label_correction, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ошибка в слове"))
        self.label_error.setText(_translate("Dialog", "Ошибка в слове:"))
        self.label_correction.setText(_translate("Dialog", "Возможно вы\n"
                                                           "имели ввиду:"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 350)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.gridLayout.addWidget(self.label_info, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_number = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_number.setFont(font)
        self.label_number.setObjectName("label_number")
        self.horizontalLayout.addWidget(self.label_number)
        self.number_in_10cc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.number_in_10cc.setFont(font)
        self.number_in_10cc.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number_in_10cc.setObjectName("number_in_10cc")
        self.horizontalLayout.addWidget(self.number_in_10cc)
        self.labe_rome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.labe_rome.setFont(font)
        self.labe_rome.setObjectName("label_rome")
        self.horizontalLayout.addWidget(self.labe_rome)
        self.number_in_rome = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.number_in_rome.setFont(font)
        self.number_in_rome.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number_in_rome.setObjectName("number_in_rome")
        self.horizontalLayout.addWidget(self.number_in_rome)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton_enter = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setObjectName("pushButton_enter")
        # ///
        self.pushButton_enter.clicked.connect(self.converter)
        # ///
        self.gridLayout.addWidget(self.pushButton_enter, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перевод числа"))
        self.label_info.setText(_translate("MainWindow", "Перевод числа из французского\n"
                                                         "языка в 10СС и римские цифры."))
        self.label_number.setText(_translate("MainWindow", "Число:"))
        self.number_in_10cc.setText(_translate("MainWindow", ""))
        self.labe_rome.setText(_translate("MainWindow", "Число в римском\n"
                                                        "формате:"))
        self.number_in_rome.setText(_translate("MainWindow", ""))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите число на французском"))
        self.pushButton_enter.setText(_translate("MainWindow", "Ввод"))

    def converter(self):
        self.word = self.lineEdit.text().lower()
        try:
            self.number = text2num(self.word, "fr")
        except ValueError:
            self.checker = SpellChecker(language='fr')
            self.correct_word = self.checker.correction(self.word)

            self.Dialog = QtWidgets.QDialog()
            self.ui_dialog = Ui_Dialog()
            self.ui_dialog.setupUi(self.Dialog)
            self.Dialog.show()

            self.ui_dialog.label.setText(self.word)
            self.ui_dialog.label_2.setText(self.correct_word)

        self.number_in_10cc.setText(str(self.number))


        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        self.syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        self.roman_num = ''
        self.i = 0
        while self.number > 0:
            for _ in range(self.number // self.val[self.i]):
                self.roman_num += self.syb[self.i]
                self.number -= self.val[self.i]
            self.i += 1
        self.number_in_rome.setText(self.roman_num)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
