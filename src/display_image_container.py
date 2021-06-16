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