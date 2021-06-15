from enum import Enum

from PyQt5.QtGui import QColor, QPalette, QBrush
from PyQt5.QtCore import pyqtSignal, QRect, QPoint, Qt, QSize
from PyQt5.QtWidgets import QLabel, QRubberBand, QHBoxLayout, QMenu

from src.utils import Utils
from src.mask_dialog import MaskDialog
from src.bounding_box import BoundingBox


class Mode(Enum):
    LABELING = 0
    CORRECTION = 1


class CorrectionMode(Enum):
    MOVE = 0
    RESIZE = 1
    OTHER = -1


class ResizeMode(Enum):
    TOP_LEFT = 0
    TOP = 1
    TOP_RIGHT = 2
    RIGHT = 3
    BOTTOM_RIGHT = 4
    BOTTOM = 5
    BOTTOM_LEFT = 6
    LEFT = 7
    OTHER = -1


class Label(Enum):
    LABEL1 = 'Head'
    LABEL2 = 'Neck'
    LABEL3 = 'Chest'
    LABEL4 = 'Abdomen'
    LABEL5 = 'Pelvis'
    LABEL6 = 'Pneumonia'
    LABEL7 = 'Cancer Nodule'
    LABEL8 = 'Tumor'


class AppString(Enum):
    APPLY_MASK = 'Наложить маску'
    EDIT_MASK = 'Редактировать маску'
    DELETE = 'Удалить метку'


class Viewer(QLabel):
    changeBoxNum = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

        self.setMouseTracking(True)
        self.__boxes = []
        self.selectedIdx = -1
        self.drawingThreshold = 30
        self.origin = QPoint()
        self.translateOffset = QPoint()
        self.__mode = Mode.LABELING
        self.__makeBoundingBox = False
        self.__correctionMode = CorrectionMode.OTHER
        self.resizeMode = ResizeMode.OTHER
        self.label = Label.LABEL1
        self.colours = [Qt.blue, Qt.yellow, Qt.darkMagenta, Qt.red, Qt.green, Qt.cyan, Qt.white, Qt.magenta] 
        self.colorTable = {Label.LABEL1: self.colours[0],
                           Label.LABEL2: self.colours[1],
                           Label.LABEL3: self.colours[2],
                           Label.LABEL4: self.colours[3],
                           Label.LABEL5: self.colours[4],
                           Label.LABEL6: self.colours[5],
                           Label.LABEL7: self.colours[6],
                           Label.LABEL8: self.colours[7]}
        self.__mouseLineVisible = True
        self.__initialize_mouse_line()
        self.__shiftFlag = False
        self.__resized = False

    def initialize(self):
        for box in self.__boxes:
            box.hide()
            box.deleteLater()

        self.__boxes.clear()
        self.selectedIdx = -1
        self.origin = QPoint()
        self.__mode = Mode.LABELING
        self.__makeBoundingBox = False
        self.__correctionMode = CorrectionMode.OTHER
        self.resizeMode = ResizeMode.OTHER
        self.label = Label.LABEL1
        self.__resized = False

    @property
    def shiftFlag(self):
        return self.__shiftFlag

    @shiftFlag.setter
    def shiftFlag(self, newFlag):
        self.__shiftFlag = newFlag

    @property
    def mouseLineVisible(self):
        return self.__mouseLineVisible

    @mouseLineVisible.setter
    def mouseLineVisible(self, flag):
        self.__mouseLineVisible = flag

        if self.__mouseLineVisible:
            for mouseLine in self.__mouseLines:
                mouseLine.show()
        else:
            for mouseLine in self.__mouseLines:
                mouseLine.hide()

    @property
    def boxes(self):
        bndBox = []

        for box in self.__boxes:
            bndBox.append([box.x(), box.y(), box.width(), box.height(), box.label])
        return bndBox

    @property
    def makeBoundingBox(self):
        return self.__makeBoundingBox

    @property
    def correctionMode(self):
        return self.__correctionMode

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, newMode):
        self.__mode = newMode

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            if self.__mode == Mode.LABELING:
                self.origin = QMouseEvent.pos()
                box = BoundingBox(QRubberBand.Line, self, self.label)
                box.setGeometry(QRect(self.origin, QSize()))
                box.geometry()
                box.setPalette(self.__set_bounding_box_color())
                box.show()
                QHBoxLayout().addWidget(box)

                self.__boxes.insert(0, box)
                self.__makeBoundingBox = True
            elif self.__mode == Mode.CORRECTION:
                selectedIdx, resizeMode = self.__find_resizing_box(QMouseEvent)

                if selectedIdx >= 0:
                    self.__correctionMode = CorrectionMode.RESIZE
                    self.resizeMode = resizeMode
                else:
                    selectedIdx = self.__find_correction_box(QMouseEvent)

                    if selectedIdx >= 0:
                        self.__correctionMode = CorrectionMode.MOVE
                        Utils.change_cursor(Qt.ClosedHandCursor)
                        self.translateOffset = QMouseEvent.pos() - self.__boxes[selectedIdx].pos()
                self.selectedIdx = selectedIdx
        super().mousePressEvent(QMouseEvent)

    def mouseMoveEvent(self, QMouseEvent):
        self.__set_mouse_line_position(QMouseEvent.pos())

        if self.__mode == Mode.CORRECTION and self.__correctionMode == CorrectionMode.OTHER:
            self.__find_resizing_box(QMouseEvent)

        if self.__mode == Mode.LABELING and self.__resized:
            if self.rect().contains(QMouseEvent.pos()):
                self.mouseLineVisible = True
                self.__set_mouse_line_position(QMouseEvent.pos())
                self.__resized = False

        if self.__makeBoundingBox:
            clipCoord = self.__clip_coordinateIn_widget(QMouseEvent)
            self.__boxes[0].setGeometry(QRect(self.origin, clipCoord).normalized())
            self.__boxes[0].geometry()
        elif self.__correctionMode != CorrectionMode.OTHER:
            selectedBox = self.__boxes[self.selectedIdx]
            if self.__correctionMode == CorrectionMode.RESIZE:

                newX, newY, newW, newH = self.__get_resize_dimension(selectedBox, QMouseEvent.pos(), self.resizeMode)

                selectedBox.setGeometry(QRect(newX, newY, newW, newH))
                selectedBox.geometry()

            elif self.__correctionMode == CorrectionMode.MOVE:
                nextCenterPosition = QMouseEvent.pos() - self.translateOffset
                nextCenterPosition.setX(max(0, min(nextCenterPosition.x(), self.width() - selectedBox.width())))
                nextCenterPosition.setY(max(0, min(nextCenterPosition.y(), self.height() - selectedBox.height())))
                selectedBox.move(nextCenterPosition)
        super().mouseMoveEvent(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        Utils.change_cursor(Qt.ArrowCursor)
        if self.__makeBoundingBox:
            if self.__boxes[0].width() * self.__boxes[0].height() < self.drawingThreshold:
                self.remove_bounding_box(0)
            else:
                self.__boxes[0].canvasPositionRatio = (self.__boxes[0].pos().x() / self.width(),
                                                       self.__boxes[0].pos().y() / self.height())
                self.__boxes[0].canvasBoxRatio = (self.__boxes[0].width() / self.width(),
                                                  self.__boxes[0].height() / self.height())
                self.changeBoxNum.emit(len(self.__boxes))
            self.__makeBoundingBox = False

        if self.__correctionMode != CorrectionMode.OTHER:
            selectedBox = self.__boxes[self.selectedIdx]
            if self.__correctionMode == CorrectionMode.RESIZE:
                selectedBox.canvasBoxRatio = (selectedBox.width() / self.width(), selectedBox.height() / self.height())
                selectedBox.canvasPositionRatio = (selectedBox.pos().x() / self.width(),
                                                   selectedBox.pos().y() / self.height())

                if selectedBox.width() * selectedBox.height() < self.drawingThreshold:
                    self.remove_bounding_box(self.selectedIdx)

                self.resizeMode = ResizeMode.OTHER

            elif self.__correctionMode == CorrectionMode.MOVE:
                selectedBox.canvasPositionRatio = (selectedBox.pos().x() / self.width(),
                                                   selectedBox.pos().y() / self.height())

            # TODO - Remove Invalid Bounding boxes with Area Threshold or Some Rules
            self.__correctionMode = CorrectionMode.OTHER

        if self.__shiftFlag:
            self.__shiftFlag = False
            self.mode = Mode.LABELING
            self.mouseLineVisible = True

        super().mouseReleaseEvent(QMouseEvent)

    def resizeEvent(self, QResizeEvent):
        if QResizeEvent.oldSize().isValid():
            newSize = QResizeEvent.size()
            for box in self.__boxes:
                box.resize(newSize.width() * box.canvasBoxRatio[0], newSize.height() * box.canvasBoxRatio[1])
                box.move(newSize.width() * box.canvasPositionRatio[0], newSize.height() * box.canvasPositionRatio[1])

            self.__resized = True
        super().resizeEvent(QResizeEvent)

    def leaveEvent(self, QEvent):
        if self.mode == Mode.LABELING:
            self.mouseLineVisible = False

    def enterEvent(self, QEvent):
        if self.mode == Mode.LABELING:
            self.mouseLineVisible = True
            self.__set_mouse_line_position(QEvent.pos())

    def contextMenuEvent(self, event):
        selectedIdx = self.__find_correction_box(event.pos())

        if selectedIdx >= 0:
            contextMenu = QMenu(self)

            contextMenu.addAction(AppString.APPLY_MASK.value)
            contextMenu.addAction(AppString.EDIT_MASK.value)
            contextMenu.addAction(AppString.DELETE.value)

            action = contextMenu.exec_(self.mapToGlobal(event.pos()))

            if action is not None:
                if action.text() == AppString.DELETE.value:
                    self.remove_bounding_box(selectedIdx)

                if action.text() == AppString.EDIT_MASK.value:
                    print(self.__boxes[selectedIdx].x(), self.__boxes[selectedIdx].x() + self.__boxes[selectedIdx].width())
                    print(self.__boxes[selectedIdx].y(), self.__boxes[selectedIdx].y() + self.__boxes[selectedIdx].height())
                    
                    self.maskDialog = MaskDialog(self, self.__boxes[selectedIdx].x(), self.__boxes[selectedIdx].x() + self.__boxes[selectedIdx].width(),
                                                 self.__boxes[selectedIdx].y(), self.__boxes[selectedIdx].y() + self.__boxes[selectedIdx].height())
                    self.maskDialog.show()

    def set_label(self, newLabel):
        self.label = Label(newLabel)

        
    def remove_bounding_box(self, idx=None):
        if idx is None:
            idx = self.selectedIdx
            self.selectedIdx = -1

        if 0 <= idx < len(self.__boxes):
            self.__boxes[idx].hide()
            self.__boxes[idx].deleteLater()
            self.__boxes.pop(idx)
            self.changeBoxNum.emit(len(self.__boxes))

    def __set_mouse_line_position(self, position):
        self.__mouseLines[0].setGeometry(QRect(QPoint(position.x(), 0), QPoint(position.x(), position.y())))
        self.__mouseLines[1].setGeometry(
            QRect(QPoint(position.x(), position.y()), QPoint(position.x(), self.height())))
        self.__mouseLines[2].setGeometry(QRect(QPoint(0, position.y()), QPoint(position.x(), position.y())))
        self.__mouseLines[3].setGeometry(
            QRect(QPoint(position.x(), position.y()), QPoint(self.width(), position.y())))

    def __initialize_mouse_line(self):
        self.__mouseLines = [QRubberBand(QRubberBand.Line, self) for _ in range(4)]

        for mouseLine in self.__mouseLines:
            mouseLine.setGeometry(QRect(QPoint(0, 0), QPoint(0, 0)))
            mouseLine.setPalette(self.__set_bounding_box_color(Label.LABEL2))
            mouseLine.show()

    def __set_bounding_box_color(self, label=None):
        if label is None:
            label = self.label

        color = QColor(self.colorTable[label])
        palette = QPalette()
        color.setAlpha(80)
        palette.setBrush(QPalette.Highlight, QBrush(color))

        return palette

    def __get_resize_dimension(self, box, mousePos, resizeMode):
        oldTopLeftX, oldTopLeftY = box.pos().x(), box.pos().y()
        oldBottomRightX, oldBottomRightY = oldTopLeftX + box.width(), oldTopLeftY + box.height()
        oldWidth, oldHeight = box.width(), box.height()

        mousePos = self.__clip_coordinateIn_widget(mousePos)

        if resizeMode == ResizeMode.TOPLEFT:
            newX, newY = mousePos.x(), mousePos.y()
            newW, newH = oldBottomRightX - mousePos.x(), oldBottomRightY - mousePos.y()

            if newW < 0 and newH < 0:
                self.resizeMode = ResizeMode.BOTTOM_RIGHT
                newH = 0
                newW = 0
                newY = oldBottomRightY
                newX = oldBottomRightX
            elif newW < 0:
                self.resizeMode = ResizeMode.TOP_RIGHT
                newW = 0
                newX = oldBottomRightX
            elif newH < 0:
                self.resizeMode = ResizeMode.BOTTOMLEFT
                newH = 0
                newY = oldBottomRightY
        elif resizeMode == ResizeMode.TOP:
            newX, newY = oldTopLeftX, mousePos.y()
            newW, newH = oldWidth, oldBottomRightY - mousePos.y()

            if newH < 0:
                self.resizeMode = ResizeMode.BOTTOM
                newH = 0
                newY = oldBottomRightY
        elif resizeMode == ResizeMode.TOP_RIGHT:
            newX, newY = oldTopLeftX, mousePos.y()
            newW, newH = mousePos.x() - oldTopLeftX, oldBottomRightY - mousePos.y()

            if newW < 0 and newH < 0:
                self.resizeMode = ResizeMode.BOTTOMLEFT
                newW = 0
                newH = 0
                newX = oldTopLeftX
                newY = oldBottomRightY
            elif newW < 0:
                self.resizeMode = ResizeMode.TOPLEFT
                newW = 0
                newX = oldTopLeftX
            elif newH < 0:
                self.resizeMode = ResizeMode.BOTTOM_RIGHT
                newH = 0
                newY = oldBottomRightY
        elif resizeMode == ResizeMode.RIGHT:
            newX, newY = oldTopLeftX, oldTopLeftY
            newW, newH = mousePos.x() - oldTopLeftX, oldHeight

            if newW < 0:
                self.resizeMode = ResizeMode.LEFT
                newW = 0
                newX = oldTopLeftX
        elif resizeMode == ResizeMode.BOTTOM_RIGHT:
            newX, newY = oldTopLeftX, oldTopLeftY
            newW, newH = mousePos.x() - oldTopLeftX, mousePos.y() - oldTopLeftY

            if newW < 0 and newH < 0:
                self.resizeMode = ResizeMode.TOPLEFT
                newW = 0
                newH = 0
                newY = oldTopLeftY
                newX = oldTopLeftX
            elif newW < 0:
                self.resizeMode = ResizeMode.BOTTOMLEFT
                newW = 0
                newX = oldTopLeftX
            elif newH < 0:
                self.resizeMode = ResizeMode.TOP_RIGHT
                newH = 0
                newY = oldTopLeftY
        elif resizeMode == ResizeMode.BOTTOM:
            newX, newY = oldTopLeftX, oldTopLeftY
            newW, newH = oldWidth, mousePos.y() - oldTopLeftY

            if newH < 0:
                self.resizeMode = ResizeMode.TOP
                newH = 0
                newY = oldTopLeftY
        elif resizeMode == ResizeMode.BOTTOMLEFT:
            newX, newY = mousePos.x(), oldTopLeftY
            newW, newH = oldBottomRightX - mousePos.x(), mousePos.y() - oldTopLeftY

            if newW < 0 and newH < 0:
                self.resizeMode = ResizeMode.TOP_RIGHT
                newW = 0
                newH = 0
                newX = oldBottomRightX
                newY = oldTopLeftY
            elif newW < 0:
                self.resizeMode = ResizeMode.BOTTOM_RIGHT
                newW = 0
                newX = oldBottomRightX
            elif newH < 0:
                self.resizeMode = ResizeMode.TOPLEFT
                newH = 0
                newY = oldTopLeftY
        elif resizeMode == ResizeMode.LEFT:
            newX, newY = mousePos.x(), oldTopLeftY
            newW, newH = oldBottomRightX - mousePos.x(), oldHeight

            if newW < 0:
                self.resizeMode = ResizeMode.RIGHT
                newW = 0
                newX = oldBottomRightX

        return newX, newY, newW, newH

    def __find_resizing_box(self, QMouseEvent):
        for idx, box in enumerate(self.__boxes):
            resizeMode = self.__set_mouse_on_edge(box, QMouseEvent)
            if resizeMode != ResizeMode.OTHER:
                return idx, resizeMode
        return -1, ResizeMode.OTHER

    def __set_mouse_on_edge(self, box: BoundingBox, QMouseEvent):
        if box.point_on_top_left(QMouseEvent):
            Utils.change_cursor(Qt.SizeFDiagCursor)
            return ResizeMode.TOPLEFT
        elif box.point_on_top(QMouseEvent):
            Utils.change_cursor(Qt.SizeVerCursor)
            return ResizeMode.TOP
        elif box.point_on_top_right(QMouseEvent):
            Utils.change_cursor(Qt.SizeBDiagCursor)
            return ResizeMode.TOP_RIGHT
        elif box.point_on_right(QMouseEvent):
            Utils.change_cursor(Qt.SizeHorCursor)
            return ResizeMode.RIGHT
        elif box.point_on_bottom_right(QMouseEvent):
            Utils.change_cursor(Qt.SizeFDiagCursor)
            return ResizeMode.BOTTOM_RIGHT
        elif box.point_on_bottom(QMouseEvent):
            Utils.change_cursor(Qt.SizeVerCursor)
            return ResizeMode.BOTTOM
        elif box.point_on_bottom_left(QMouseEvent):
            Utils.change_cursor(Qt.SizeBDiagCursor)
            return ResizeMode.BOTTOMLEFT
        elif box.point_on_left(QMouseEvent):
            Utils.change_cursor(Qt.SizeHorCursor)
            return ResizeMode.LEFT
        else:
            Utils.change_cursor(Qt.ArrowCursor)
            return ResizeMode.OTHER

    def __clip_coordinateIn_widget(self, QMouseEvent):
        clipCoord = QPoint()
        clipCoord.setX(max(0, min(QMouseEvent.x(), self.width())))
        clipCoord.setY(max(0, min(QMouseEvent.y(), self.height())))

        return clipCoord

    def __find_correction_box(self, QMouseEvent):
        for idx, box in enumerate(self.__boxes):
            if self.__set_mouse_in_box(QMouseEvent, box):
                return idx
        return -1

    def __set_mouse_in_box(self, QMouseEvent, box):
        inX = box.x() <= QMouseEvent.x() < box.x() + box.width()
        inY = box.y() <= QMouseEvent.y() < box.y() + box.height()
        return inX and inY