import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from src.utils import Utils
from src.label_set import LabelSet
from src.dicom_image import DicomImage
from src.main_window import MainWindow

class Application(QMainWindow, MainWindow):
    dicomImage: DicomImage

    def __init__(self):
        super().__init__()
        Utils.change_cursor(Qt.WaitCursor)
        self.setupUi()
        self.show()

    def initialize(self):
        self.loadImage = None
        self.dicomImage = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Application()
    LabelSet.deleteFile()
    sys.exit(app.exec_())