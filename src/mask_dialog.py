import cv2

from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets


class MaskDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, x_min=0, x_max=0, y_min=0, y_max=0):
        super(MaskDialog, self).__init__(parent)
        self.setWindowTitle('Редактирование маски')
        self.setStyleSheet("font: 75 12pt \"Arial Narrow\";\n"
                           "border-color: rgb(85, 87, 83);\n"
                           "color: rgb(255, 255, 255);\n"
                           "background-color: rgb(85, 87, 83);")
        self.setMinimumSize(400, 580)
        self.setMaximumSize(400, 580)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.valueChanged.connect(self.dilatationValueChange)
        self.horizontalLayout_2.addWidget(self.horizontalSlider_2)
        self.label_3 = QtWidgets.QLabel("    0", self.groupBox_2)
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton("Сохранить маску", self.groupBox_2)
        self.pushButton1.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                      "color: rgb(46, 52, 54);")
        self.pushButton1.clicked.connect(self.exit)
        self.gridLayout.addWidget(self.pushButton1, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel("Значение дилатации", self.groupBox_2)
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel("Значение эрозии", self.groupBox_2)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.valueChanged.connect(self.erosionValueChange)
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel("    0", self.groupBox_2)
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 350))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        img = cv2.imread('./.temp/temp.png')
        img1 = img[y_min:y_max, x_min:x_max]
        cv2.imwrite('./.temp/temp.png', img1)
        self.label_5.setPixmap(QPixmap('./.temp/temp.png'))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

    def erosionValueChange(self):
        erosionValue = self.horizontalSlider.value()
        self.label_2.setText(str(erosionValue))

    def dilatationValueChange(self):
        dilatationValue = self.horizontalSlider_2.value()
        self.label_3.setText(str(dilatationValue))

    def exit(self):
        self.close()