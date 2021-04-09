from PyQt5.QtWidgets import QRubberBand


class BoundingBox(QRubberBand):
    def __init__(self, shape, parent, label):
        super().__init__(shape, parent)
        self.pointCheckRange = 3
        self.canvasPositionRatio = (0, 0)
        self.canvasBoxRatio = (0, 0)
        self.label = label

    def point_on_top_left(self, pos):
        return (self.x() <= pos.x() < self.x() + self.pointCheckRange) and \
               (self.y() <= pos.y() < self.y() + self.pointCheckRange)

    def point_on_top(self, pos):
        return (self.x() + self.pointCheckRange <= pos.x() < self.x() + self.width() - self.pointCheckRange) and \
               (self.y() <= pos.y() < self.y() + self.pointCheckRange)

    def point_on_top_right(self, pos):
        return (self.x() + self.width() - self.pointCheckRange <= pos.x() < self.x() + self.width()) and \
               (self.y() <= pos.y() < self.y() + self.pointCheckRange)

    def point_on_right(self, pos):
        return (self.x() + self.width() - self.pointCheckRange <= pos.x() < self.x() + self.width()) and \
               (self.y() + self.pointCheckRange <= pos.y() < self.y() + self.height() - self.pointCheckRange)

    def point_on_bottom_right(self, pos):
        return (self.x() + self.width() - self.pointCheckRange <= pos.x() < self.x() + self.width()) and \
               (self.y() + self.height() - self.pointCheckRange <= pos.y() < self.y() + self.height())

    def point_on_bottom(self, pos):
        return (self.x() + self.pointCheckRange <= pos.x() < self.x() + self.width() - self.pointCheckRange) and \
               (self.y() + self.height() - self.pointCheckRange <= pos.y() < self.y() + self.height())

    def point_on_bottom_left(self, pos):
        return (self.x() <= pos.x() < self.x() + self.pointCheckRange) and \
               (self.y() + self.height() - self.pointCheckRange <= pos.y() < self.y() + self.height())

    def point_on_left(self, pos):
        return (self.x() <= pos.x() < self.x() + self.pointCheckRange) and \
               (self.y() + self.pointCheckRange <= pos.y() < self.y() + self.height() - self.pointCheckRange)
