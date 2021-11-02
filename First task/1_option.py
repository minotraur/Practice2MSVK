from text_to_num import text2num
from spellchecker import SpellChecker
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        MainWindow.setMinimumSize(QtCore.QSize(900, 500))
        MainWindow.setMaximumSize(QtCore.QSize(900, 500))
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, -10, 354, 87))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(390, 200, 86, 29))
        font = QtGui.QFont()
        font.setFamily("Literata 12pt")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 250, 352, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.labelTwoWordError = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Literata 12pt")
        font.setPointSize(14)
        self.labelTwoWordError.setFont(font)
        self.labelTwoWordError.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelTwoWordError.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTwoWordError.setObjectName("labelTwoWordError")
        self.gridLayout_9.addWidget(self.labelTwoWordError, 0, 0, 1, 1)
        self.TwoWordError = QtWidgets.QLabel(self.layoutWidget)
        self.TwoWordError.setMinimumSize(QtCore.QSize(350, 100))
        self.TwoWordError.setMaximumSize(QtCore.QSize(301, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TwoWordError.setFont(font)
        self.TwoWordError.setStyleSheet("color: rgb(255, 255, 255);")
        self.TwoWordError.setText("")
        self.TwoWordError.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.TwoWordError.setObjectName("TwoWordError")
        self.gridLayout_9.addWidget(self.TwoWordError, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 251, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_enter = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_enter.setFont(font)
        self.lineEdit_enter.setStyleSheet("border: 1px solid white;\n"
                                          "text-decoration: none;\n"
                                          "background-color: rgb(51, 51, 54);\n"
                                          "color: rgb(255, 255, 255);")
        self.lineEdit_enter.setObjectName("lineEdit_enter")
        self.gridLayout_4.addWidget(self.lineEdit_enter, 0, 0, 1, 1)
        self.pushButton_enter = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_enter.setFont(font)
        self.pushButton_enter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_enter.setStyleSheet("QPushButton#pushButton_enter{\n"
                                            "    background-color: rgb(51, 51, 54);\n"
                                            "    border: 1px solid white;\n"
                                            "    border-radius: 5px;\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton#pushButton_enter:pressed{\n"
                                            "    background-color: rgb(40, 149, 0);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "")
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.gridLayout_4.addWidget(self.pushButton_enter, 1, 0, 1, 1)
        self.pushButton_enter.clicked.connect(self.converter)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 80, 398, 97))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.num_in_10cc = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_in_10cc.setFont(font)
        self.num_in_10cc.setStyleSheet("color: rgb(255, 255, 255);")
        self.num_in_10cc.setText("")
        self.num_in_10cc.setObjectName("num_in_10cc")
        self.gridLayout_2.addWidget(self.num_in_10cc, 0, 1, 1, 1)
        self.num_in_rome = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_in_rome.setFont(font)
        self.num_in_rome.setStyleSheet("color: rgb(255, 255, 255);")
        self.num_in_rome.setText("")
        self.num_in_rome.setObjectName("num_in_rome")
        self.gridLayout_2.addWidget(self.num_in_rome, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(40, 250, 321, 171))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelErrorInWord = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelErrorInWord.setFont(font)
        self.labelErrorInWord.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelErrorInWord.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelErrorInWord.setObjectName("labelErrorInWord")
        self.gridLayout_5.addWidget(self.labelErrorInWord, 0, 0, 1, 1)
        self.ErrorInWord = QtWidgets.QLabel(self.layoutWidget3)
        self.ErrorInWord.setMinimumSize(QtCore.QSize(301, 100))
        self.ErrorInWord.setMaximumSize(QtCore.QSize(301, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ErrorInWord.setFont(font)
        self.ErrorInWord.setStyleSheet("color: rgb(255, 255, 255);")
        self.ErrorInWord.setText("")
        self.ErrorInWord.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ErrorInWord.setObjectName("ErrorInWord")
        self.gridLayout_5.addWidget(self.ErrorInWord, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перевод числа"))
        self.label.setText(_translate("MainWindow", "Перевод числа с французского языка\n"
                                                    "в десятичное представление\n"
                                                    "и римские цифры"))
        self.label_6.setText(_translate("MainWindow", "Ошибки:"))
        self.labelTwoWordError.setText(_translate("MainWindow", ""))
        self.lineEdit_enter.setPlaceholderText(_translate("MainWindow", "Введите число на французском"))
        self.pushButton_enter.setText(_translate("MainWindow", "Подтвердить"))
        self.label_4.setText(_translate("MainWindow", "Римское\n"
                                                      "число:"))
        self.label_3.setText(_translate("MainWindow", "Число\n"
                                                      " в 10СС:"))
        self.label_2.setText(_translate("MainWindow", "Вывод:"))
        self.labelErrorInWord.setText(_translate("MainWindow", ""))

    def converter(self):
        self.labelErrorInWord.clear()
        self.ErrorInWord.clear()

        self.labelTwoWordError.clear()
        self.TwoWordError.clear()

        self.word = self.lineEdit_enter.text().lower().strip().replace('  ', ' ')

        self.temp_word = self.word.split(' ')

        self.words = ['une',
                      'deux',
                      'trois',
                      'quatre',
                      'cinq',
                      'six',
                      'Sept',
                      'huit',
                      'neuf',
                      'dix',
                      'onze',
                      'douze',
                      'treize',
                      'quatorze',
                      'quinze',
                      'seize',
                      'dix sept',
                      'dix huit',
                      'dix neuf',
                      'vingt',
                      'trente',
                      'quarante',
                      'cinquante',
                      'soixante',
                      'soixante dix',
                      'quatre vingt',
                      'quatre vingt dix',
                      'cent',
                      'mille', ]

        try:
            self.number = text2num(self.word, "fr")
        except ValueError:
            self.checker = SpellChecker(language='fr')
            for idx, word in enumerate(self.temp_word):
                if word not in self.words:
                    self.labelErrorInWord.setText('Ошибка в слове')
                    self.ErrorInWord.setText(word)

        for curr, next in zip(self.temp_word, self.temp_word[1:]):
            if curr == next:
                self.labelTwoWordError.setText('Одинаковые слова')
                self.TwoWordError.setText(f'{curr}')

                self.labelErrorInWord.clear()
                self.ErrorInWord.clear()

        self.num_in_10cc.setText(str(self.number))

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
        self.num_in_rome.setText(self.roman_num)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
