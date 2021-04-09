from PyQt5 import QtCore, QtGui, QtWidgets

class MaskDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MaskDialog, self).__init__(parent)
        self.setWindowTitle('Наложение маски')
        self.setStyleSheet("font: 75 10pt \"Umpush\";\n"
                           "border-color: rgb(85, 87, 83);\n"
                           "color: rgb(255, 255, 255);\n"
                           "background-color: rgb(85, 87, 83);")
        self.setMinimumSize(350, 500)
        self.setMaximumSize(350, 500)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.verticalLayout.addWidget(self.graphicsView)
        self.erosionLabel = QtWidgets.QLabel('Значение эрозии', self)
        self.verticalLayout.addWidget(self.erosionLabel)
        self.erosionSplitter = QtWidgets.QSplitter(self)
        self.erosionSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.erosionHorizontalSlider = QtWidgets.QSlider(self.erosionSplitter)
        self.erosionHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.erosionValue = QtWidgets.QLabel('  0', self.erosionSplitter)
        self.verticalLayout.addWidget(self.erosionSplitter)
        self.dilatationLabel = QtWidgets.QLabel('Значение дилатации', self)
        self.verticalLayout.addWidget(self.dilatationLabel)
        self.dilatationSplitter = QtWidgets.QSplitter(self)
        self.dilatationSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.dilatationHorizontalSlider = QtWidgets.QSlider(self.dilatationSplitter)
        self.dilatationHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.dilatationValue = QtWidgets.QLabel('  0', self.dilatationSplitter)
        self.verticalLayout.addWidget(self.dilatationSplitter)
        self.pushButton = QtWidgets.QPushButton('Наложить маску', self)
        self.pushButton.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                      "color: rgb(46, 52, 54);")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)