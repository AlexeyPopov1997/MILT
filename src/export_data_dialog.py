from PyQt5 import QtWidgets


class ExportDataDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ExportDataDialog, self).__init__(parent)
        self.setWindowTitle('Экспорт данных')
        self.setStyleSheet("font: 75 12pt \"Arial Narrow\";\n"
                           "border-color: rgb(85, 87, 83);\n"
                           "color: rgb(255, 255, 255);\n"
                           "background-color: rgb(85, 87, 83);")
        self.setMinimumSize(400, 380)
        self.setMaximumSize(400, 380)
        self.gridLayout3 = QtWidgets.QGridLayout(self)
        self.groupBox = QtWidgets.QGroupBox('Серия изображений', self)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel('Использовать текущий путь', self.groupBox)
        self.horizontalLayout2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout2.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.horizontalLayout2.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label2 = QtWidgets.QLabel('Выбрать серию снимков', self.groupBox)
        self.horizontalLayout.addWidget(self.label2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton('Обзор...', self.groupBox)
        self.pushButton.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                      "color: rgb(46, 52, 54);")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox3 = QtWidgets.QGroupBox('Сохранение', self)
        self.gridLayout2 = QtWidgets.QGridLayout(self.groupBox3)
        self.horizontalLayout3 = QtWidgets.QHBoxLayout()
        self.label4 = QtWidgets.QLabel('Сохранить в корень', self.groupBox3)
        self.horizontalLayout3.addWidget(self.label4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem2)
        self.checkBox2 = QtWidgets.QCheckBox(self.groupBox3)
        self.horizontalLayout3.addWidget(self.checkBox2)
        self.gridLayout2.addLayout(self.horizontalLayout3, 0, 0, 1, 1)
        self.horizontalLayout4 = QtWidgets.QHBoxLayout()
        self.label5 = QtWidgets.QLabel('Выбрать место сохранения', self.groupBox3)
        self.horizontalLayout4.addWidget(self.label5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout4.addItem(spacerItem3)
        self.pushButton2 = QtWidgets.QPushButton('Обзор...', self.groupBox3)
        self.pushButton2.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                        "color: rgb(46, 52, 54);")
        self.horizontalLayout4.addWidget(self.pushButton2)
        self.gridLayout2.addLayout(self.horizontalLayout4, 1, 0, 1, 1)
        self.gridLayout3.addWidget(self.groupBox3, 2, 0, 1, 1)

        self.groupBox6 = QtWidgets.QGroupBox(self)
        self.horizontalLayout6 = QtWidgets.QHBoxLayout()
        self.pushButton3 = QtWidgets.QPushButton('Экспорт', self.groupBox6)
        self.pushButton3.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                        "color: rgb(46, 52, 54);")
        self.pushButton3.clicked.connect(self.export)
        self.horizontalLayout6.addWidget(self.pushButton3)
        self.gridLayout3.addLayout(self.horizontalLayout6, 3, 0, 1, 1)
        self.gridLayout3.addWidget(self.groupBox6, 3, 0, 1, 1)

    def export(self):
        self.close()
        