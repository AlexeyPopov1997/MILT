import pydicom
import numpy as np

from pydicom.datadict import DicomDictionary, keyword_dict
from pydicom.pixel_data_handlers.numpy_handler import pack_bits


class DicomImage:
    def __init__(self, image, filePath):
        self.__image = image
        self.__image = pydicom.read_file(filePath)
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
    def imageHeight(self):
        pixelArray = self.image.pixel_array
        height = pixelArray.shape[0]
        return height

    @property
    def imageWidth(self):
        pixelArray = self.image.pixel_array
        width = pixelArray.shape[1]
        return width

    def create_overlay_box(self, x_min, y_min, x_max, y_max):
        boundBox = self.image.pixel_array
        for i in range(len(boundBox)):
            for j in range(len(boundBox[i])):
                boundBox[i][j] = 0

        boundBox[y_min, x_min:x_max] = 1
        boundBox[y_max, x_min:x_max] = 1
        boundBox[y_min:y_max, x_min] = 1
        boundBox[y_min:y_max, x_max] = 1
        return boundBox

    def add_overlay(self, label, overlayBbox):
        groups = {
         'Head': 0x6000,
         'Neck': 0x6002,
         'Chest': 0x6004,
         'Abdomen': 0x6006,
         'Pelvis': 0x6008,
        }

        string = label + ': Overlay Rows'

        newDictItems = {
            (groups[label], 0x0010): ('US', '1', string, '', 'OverlayRows'),
            (groups[label], 0x0011): ('US', '1', label + ": Overlay Columns", '', 'OverlayColumns'),
            (groups[label], 0x0015): ('IS', '1', label + ": Number of Frames in Overlay", '', 'NumberFrames'),
            (groups[label], 0x0022): ('LO', '1', label + ": Overlay Description ", '', 'OverlayDescription'),
            (groups[label], 0x0040): ('CS', '1', label + ": Overlay Type", '', 'OverlayType'),
            (groups[label], 0x0050): ('SS', '2', label + ": Overlay Origin", '', 'OverlayOrigin'),
            (groups[label], 0x0051): ('US', '1', label + ": Image Frame Origin ", '', 'ImageFrameOrigin'),
            (groups[label], 0x0100): ('US', '1', label + ": Overlay Bits Allocated", '', 'OverlayBitsAllocated'),
            (groups[label], 0x0102): ('US', '1', label + ": Overlay Bit Position", '', 'OverlayBitPosition'),
            (groups[label], 0x3000): ('OW', '1', label + ": Overlay Data", '', 'OverlayData'),
        }

        DicomDictionary.update(newDictItems)
        newNamesDict = dict([(val[4], tag) for tag, val in newDictItems.items()])
        keyword_dict.update(newNamesDict)
        rowCount, colCount = overlayBbox.shape
        self.image.OverlayRows = rowCount
        self.image.OverlayColumns = colCount
        self.image.NumberFrames = 1
        self.image.OverlayDescription = label
        self.image.OverlayType = 'G'
        self.image.OverlayOrigin = [1, 1]
        self.image.ImageFrameOrigin = 1
        self.image.OverlayBitsAllocated = 1
        self.image.OverlayBitPosition = 0
        overlayBboxNew = np.reshape(overlayBbox, overlayBbox.size)
        packedBytes = pack_bits(overlayBboxNew)

        if len(packedBytes) % 2:
            packedBytes += b'\x00'

        self.image.OverlayData = packedBytes
        self.image[groups[label], 0x3000].VR = 'OW'
        return self.image
