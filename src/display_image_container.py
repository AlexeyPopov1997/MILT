import os
from typing import List
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication


class Utils:
    @staticmethod
    def change_cursor(cursorShape):
        QApplication.setOverrideCursor(QCursor(cursorShape))

    @staticmethod
    def isDicomFile(path: str) -> bool:
        if not os.path.isfile(path):
            return False
        try:
            with open(path, "rb") as f:
                return f.read(132).decode("ASCII")[-4:] == "DICM"
        except:
            return False

    @staticmethod
    def dicomFilesInDir(directory: str = ".") -> List[str]:
        directory = os.path.expanduser(directory)
        candidates = [os.path.join(directory, f) for f in sorted(os.listdir(directory))]
        return [f for f in candidates if Utils.isDicomFile(f)]


class DisplayImageContainer:
    def __init__(self, image, filePath):
        self.__image = image
        self.__imageWidth = image.width() if image is not None else 0
        self.__imageHeight = image.height() if image is not None else 0
        self.__filePath = filePath

    @property
    def image(self):
        return self.__image

    @property
    def filePath(self):
        return self.__filePath

    @property
    def fileName(self):
        return self.__filePath.split('\\')[-1].split('/')[-1]

    @property
    def imageWidth(self):
        return self.__imageWidth

    @property
    def imageHeight(self):
        return self.__imageHeight
