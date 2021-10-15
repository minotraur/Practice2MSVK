from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 352)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        self.pushButton.clicked.connect(self.some_work_lol)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.label_result.setFont(font)
        self.label_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout_2.addWidget(self.label_result, 1, 0, 1, 1)
        self.result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout_2.addWidget(self.result, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Слова в шахматном порядке наоборот"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите слова через пробел"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите слова через пробел"))
        self.pushButton.setText(_translate("MainWindow", "Подтвердить"))
        self.label_result.setText(_translate("MainWindow", "Результат"))

    def some_work_lol(self):
        self.string_1 = self.lineEdit.text().strip().replace('  ', ' ').split(' ')
        self.string_2 = self.lineEdit_2.text().strip().replace('  ', ' ').split(' ')

        self.new_mas = []

        self.index_from_string2 = 1
        self.i = 0
        self.length_string2 = len(self.string_2)

        while self.length_string2 != 0:
            self.string_1.insert(self.index_from_string2, self.string_2[self.i])
            self.i += 1
            self.index_from_string2 += 2
            self.length_string2 -= 1

        an = len(self.string_1) - 1
        while an != -1:
            self.new_mas.append(self.string_1[an])
            an -= 1

        self.result.setText(' '.join(self.new_mas))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
