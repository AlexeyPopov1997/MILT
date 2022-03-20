import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# Import GUI
from ui.main_ui import MainWindowUi

# Import funstions for GUI
from ui.ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainWindowUi()
        self.ui.setup_ui(self)

        # Move window
        def moveWindow(event):
            # Restore before move
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # If left click move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Set title bar
        self.ui.title_bar_frame.mouseMoveEvent = moveWindow

        # Set taskbar logo
        self.setWindowIcon(QtGui.QIcon('./icons/taskbar_logo.png'))

        # Set GUI definitions
        UIFunctions.uiDefinitions(self)

        # Show main window
        self.show()

    ## App events
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
