from PyQt5 import QtCore, QtGui, QtWidgets


class ExportDataDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ExportDataDialog, self).__init__(parent)
        self.setWindowTitle('Экспорт сериализированных данных')
        self.setStyleSheet("font: 75 10pt \"Umpush\";\n"
                           "border-color: rgb(85, 87, 83);\n"
                           "color: rgb(255, 255, 255);\n"
                           "background-color: rgb(85, 87, 83);")
        self.setMinimumSize(400, 380)
        self.setMaximumSize(400, 380)
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.groupBox = QtWidgets.QGroupBox('Серия изображений', self)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel('Использовать текущий путь', self.groupBox)
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label_2 = QtWidgets.QLabel('Выбрать серию снимков', self.groupBox)
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton('Обзор...', self.groupBox)
        self.pushButton.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                      "color: rgb(46, 52, 54);")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox('Классы поиска', self)
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 30, 311, 61))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QtWidgets.QLabel('Укажите классы поиска (через пробел)', self.widget)
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                    "color: rgb(46, 52, 54);")
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox('Сохранение', self)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.label_4 = QtWidgets.QLabel('Сохранить в корень', self.groupBox_3)
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.horizontalLayout_3.addWidget(self.checkBox_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_5 = QtWidgets.QLabel('Выбрать место сохранения', self.groupBox_3)
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton('Обзор...', self.groupBox_3)
        self.pushButton_2.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                        "color: rgb(46, 52, 54);")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 1)