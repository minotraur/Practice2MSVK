import re
from tkinter import messagebox

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def __init__(self):
        self.line = ''
        self.first = ''
        self.second = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit_sequence = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sequence.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_sequence.setFont(font)
        self.lineEdit_sequence.setObjectName("lineEdit_sequence")
        self.gridLayout.addWidget(self.lineEdit_sequence, 1, 0, 1, 2)
        self.pushButton_sequence = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sequence.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_sequence.setObjectName("pushButton_sequence")

        # Кнопка подтверждения
        self.pushButton_sequence.clicked.connect(self.work)

        self.gridLayout.addWidget(self.pushButton_sequence, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.label_entered_sequence = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_entered_sequence.setFont(font)
        self.label_entered_sequence.setText("")
        self.label_entered_sequence.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_entered_sequence.setObjectName("label_entered_sequence")
        self.gridLayout.addWidget(self.label_entered_sequence, 4, 0, 1, 2)
        self.lineEdit_word_one = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_word_one.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_word_one.setFont(font)
        self.lineEdit_word_one.setObjectName("lineEdit_word_one")
        self.gridLayout.addWidget(self.lineEdit_word_one, 5, 0, 1, 1)
        self.lineEdit_word_two = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_word_two.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_word_two.setFont(font)
        self.lineEdit_word_two.setObjectName("lineEdit_word_two")
        self.gridLayout.addWidget(self.lineEdit_word_two, 5, 1, 1, 1)
        self.pushButton_rearrange = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rearrange.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_rearrange.setObjectName("pushButton_rearrange")

        # Кнопка перестановки
        self.pushButton_rearrange.clicked.connect(self.rerange)

        self.gridLayout.addWidget(self.pushButton_rearrange, 6, 0, 1, 2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 2)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 8, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label.setText(_translate("MainWindow", "Перестановка в последовательности(в конец)"))
        self.lineEdit_sequence.setPlaceholderText(_translate("MainWindow", "введите последовательность"))
        self.pushButton_sequence.setText(_translate("MainWindow", "Подтвердить последовательность"))
        self.label_2.setText(_translate("MainWindow", "Введённая последовательность"))
        self.lineEdit_word_one.setPlaceholderText(_translate("MainWindow", "введите слово"))
        self.lineEdit_word_two.setPlaceholderText(_translate("MainWindow", "введите слово"))
        self.pushButton_rearrange.setText(_translate("MainWindow", "Переставить"))
        self.label_3.setText(_translate("MainWindow", "Результат"))

    def work(self):
        entered = ' '.join(self.lineEdit_sequence.text().split())
        self.line = entered.strip().lower()
        print(self.line)
        if self.line == '':
            self.label_entered_sequence.setText('Вы не ввели последовательность')
        else:
            self.label_entered_sequence.setText(self.line)

    def rerange(self):
        testline = self.line.split(' ')

        if not self.lineEdit_word_one.text() and not self.lineEdit_word_two.text():
            self.label_result.setText('Вы не ввели слова')
        elif not self.lineEdit_word_one.text():
            self.label_result.setText('Вы не ввели первое слово')
        elif not self.lineEdit_word_two.text():
            self.label_result.setText('Вы не ввели второе слово')
        else:

            self.first = ' '.join(self.lineEdit_word_one.text().split()).strip().lower()
            self.second = ' '.join(self.lineEdit_word_two.text().split()).strip().lower()

            if self.first == self.second:
                self.label_result.setText('Вы ввели одинаковые слова')
            elif self.first not in testline:
                self.label_result.setText('Слово \'{}\' не существует в последовательности!'.format(self.first))
            elif self.first and self.second in testline:
                words = self.line.split(' ')
                some_word = None
                some_word2 = None
                for i, word in enumerate(words):
                    if word.startswith(self.first):
                        some_word = word
                        del words[i]
                        break

                for i, word in enumerate(words):
                    if word.startswith(self.second):
                        some_word2 = word
                        del words[i]
                        break

                words.append(some_word)
                words.append(some_word2)
                self.label_result.setText(' '.join(words))

            elif self.second not in testline:
                self.label_result.setText('Слово \'{}\' не существует в последовательности!'.format(self.second))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
