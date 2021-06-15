import os
from typing import List
import SimpleITK as stk

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QGridLayout, QGroupBox, QVBoxLayout, \
                            QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QComboBox, \
                            QListWidget, QLabel, QMenu, QFileDialog, QListWidgetItem

from src.utils import Utils
from src.viewer import Viewer
from src.label_set import LabelSet
from src.dicom_image import DicomImage
from src.export_data_dialog import ExportDataDialog
from src.display_image_container import DisplayImageContainer


class MainWindow:
    def __init__(self):
        super().__init__()
        self.resize(1150, 800)
        self.setMinimumSize(QSize(880, 634))
        self.setMaximumSize(QSize(880, 634))
        self.setWindowTitle("MILT.DICOM")
        self.allowImageType = '(*.dcm)'

    def buildWorkingArea(self):
        self.workingAreaGroupBox = QGroupBox("Рабочая область", self.centralwidget)
        self.verticalLayoutWorkingArea = QVBoxLayout(self.workingAreaGroupBox)
        self.horizontalLayoutWorkingArea = QHBoxLayout()
        # Spacer
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayoutWorkingArea.addItem(spacerItem)
        # Line Edit
        self.lineEdit = QLineEdit(self.workingAreaGroupBox)
        self.lineEdit.setMinimumSize(QSize(200, 30))
        self.lineEdit.setMaximumSize(QSize(260, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                    "color: rgb(46, 52, 54);")
        self.lineEdit.setPlaceholderText("Добавить новый класс...")
        self.lineEdit.returnPressed.connect(self.lineEditOnPressed)
        self.horizontalLayoutWorkingArea.addWidget(self.lineEdit)
        # Combo Box
        self.comboBox = QComboBox(self.workingAreaGroupBox)
        self.comboBox.setMinimumSize(QSize(200, 30))
        self.comboBox.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                    "color: rgb(46, 52, 54);")
        self.horizontalLayoutWorkingArea.addWidget(self.comboBox)
        self.verticalLayoutWorkingArea.addLayout(self.horizontalLayoutWorkingArea)
        # Work Area Graphics View
        self.graphicsView = Viewer(self)
        self.graphicsView.setScaledContents(True)
        self.graphicsView.setFocusPolicy(Qt.StrongFocus)
        self.graphicsView.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.verticalLayoutWorkingArea.addWidget(self.graphicsView)
        self.gridLayoutMain.addWidget(self.workingAreaGroupBox, 0, 1, 2, 1)

    
    def buildImagesListArea(self):
        self.imagesListGroupBox = QGroupBox("Изображения серии", self.centralwidget)
        self.imagesListGroupBox.setMinimumSize(QSize(320, 150))
        self.imagesListGroupBox.setMaximumSize(QSize(320, 999999))
        self.gridLayout = QGridLayout(self.imagesListGroupBox)
        self.listView = QListWidget(self.imagesListGroupBox)
        self.listView.setStyleSheet("background-color: rgb(186, 189, 182);\n"
                                    "color: rgb(46, 52, 54);")
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.gridLayoutMain.addWidget(self.imagesListGroupBox, 0, 0, 1, 1)
        self.listView.itemSelectionChanged.connect(self.onFileItemChange)


    def buildLogoArea(self):
        self.logoAreaGroupBox = QGroupBox(self.centralwidget)
        self.logoAreaGroupBox.setMinimumSize(QSize(320, 120))
        self.logoAreaGroupBox.setMaximumSize(QSize(320, 120))
        self.verticalLayout = QVBoxLayout(self.logoAreaGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self.logoAreaGroupBox)
        self.label.setPixmap(QPixmap("icons/logo.png"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayoutMain.addWidget(self.logoAreaGroupBox, 1, 0, 1, 1)

    
    def buidMenuBar(self):
        self.menuBar().setStyleSheet("background-color: rgb(85, 87, 83);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: 75 10pt bold \"Arial Narrow\";")
                                     
        self.fileMenu = QMenu('Файл', self)
        self.fileMenu.setStyleSheet("background-color: rgb(85, 87, 83);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 10pt bold \"Arial Narrow\";")

        self.fileMenu.addAction("Открыть DICOM-файл", self.openFileDialogue)                          
        self.fileMenu.addAction("Открыть серию", self.openFolder)
        self.fileMenu.addAction("Сохранить DICOM-файл")
        self.fileMenu.addAction("Настройки")

        self.menuBar().addMenu(self.fileMenu)

        self.toolsMenu = QMenu('Инструменты', self)
        self.toolsMenu.setStyleSheet("background-color: rgb(85, 87, 83);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 10pt bold \"Arial Narrow\";")
        
        self.toolsMenu.addAction("Экспорт данных в COCO", self.openExportDataDialog)
        self.toolsMenu.addAction("Экспорт данных в Pascal VOC", self.openExportDataDialog)
        self.toolsMenu.addAction("Экспорт данных в YOLO", self.openExportDataDialog)

        self.menuBar().addMenu(self.toolsMenu)

        self.helpMenu = QMenu('Помощь', self)
        self.helpMenu.setStyleSheet("background-color: rgb(85, 87, 83);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 75 10pt bold \"Arial Narrow\";")

        self.helpMenu.addAction("Начало работы")
        self.menuBar().addMenu(self.helpMenu)


    def setupUi(self):
        self.buidMenuBar()
        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("font: 75 12pt \"Arial Narrow\";\n"
                                         "border-color: rgb(85, 87, 83);\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(85, 87, 83);")

        self.gridLayoutMain = QGridLayout(self.centralwidget)

        self.buildWorkingArea()
        self.buildImagesListArea()
        self.buildLogoArea()
        self.setCentralWidget(self.centralwidget)

    def lineEditOnPressed(self):
        text = self.lineEdit.text()
        LabelSet.addLabel(text)
        self.comboBox.addItem(text)
        self.comboBox.currentTextChanged.connect(self.graphicsView.set_label)
        self.lineEdit.clear()

    def openFileDialogue(self):
        imagePath, fileType = QFileDialog.getOpenFileName(self, 'Select Image', '',
                                                          'Image files {}'.format(self.allowImageType),
                                                          options=QFileDialog.DontUseNativeDialog)

        if imagePath != '':
            img = stk.ReadImage(imagePath)
            img = stk.IntensityWindowing(img, -1000, 1000, 0, 255)
            img = stk.Cast(img, stk.sitkUInt8)
            stk.WriteImage(img, "./.temp/temp.png")
            rawImage = QImage('./.temp/temp.png')

            self.initialize()
            self.graphicsView.initialize()
            self.loadImage = DisplayImageContainer(rawImage, imagePath)
            self.dicomImage = DicomImage(rawImage, imagePath)
            self.graphicsView.setPixmap(QPixmap.fromImage(rawImage.scaled(self.graphicsView.width(), self.graphicsView.height())))
    
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        try:
            self._file_name = value

            if self._file_name != '':
                img = stk.ReadImage(self._file_name)
                img = stk.IntensityWindowing(img, -1000, 1000, 0, 255)
                img = stk.Cast(img, stk.sitkUInt8)
                stk.WriteImage(img, "./.temp/temp.png")
                rawImage = QImage('./.temp/temp.png')

                self.initialize()
                self.loadImage = DisplayImageContainer(rawImage, self._file_name)
                self.dicomImage = DicomImage(rawImage, self._file_name)
                self.graphicsView.setPixmap(QPixmap.fromImage(rawImage.scaled(self.graphicsView.width(), self.graphicsView.height())))

        except BaseException as exc:
            print(exc)

    def openFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setViewMode(QFileDialog.List)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        if dialog.exec_():
            directory = str(dialog.selectedFiles()[0])
            self.loadFiles(Utils.dicomFilesInDir(directory))
        print(self.graphicsView.size())
            
    def onFileItemChange(self):
        if not len(self.listView.selectedItems()):
            self.file_name = None
        else:
            item = self.listView.selectedItems()[0]
            self.file_name = str(item.toolTip())

    def loadFiles(self, files: List[str]):
        self.listView.clear()
        self.files = files
        for file_name in self.files:
            item = QListWidgetItem(os.path.basename(file_name))
            item.setToolTip(file_name)
            self.listView.addItem(item)
        self.listView.setMinimumWidth(self.listView.sizeHintForColumn(0) + 20)
        if self.files:
            self.file_name = self.files[0]

    def openExportDataDialog(self):
        self.exportDataDialog = ExportDataDialog(self)
        self.exportDataDialog.show()