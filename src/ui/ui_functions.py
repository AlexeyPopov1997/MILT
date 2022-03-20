from main import *

from .style_sheet import StyleSheet


GLOBAL_STATE = 0


class UIFunctions(MainWindow):
    # Maximize restore function
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # If not miximized
        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            # If miximized remove margins
            self.ui.central_widget_vertical_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.central_widget_frame.setStyleSheet(StyleSheet.get_restore_window_style())
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.central_widget_vertical_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.central_widget_frame.setStyleSheet(StyleSheet.get_maximize_windwow_style())

    # GUI Definitions
    def uiDefinitions(self):
        # Remove standard border
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set dropshadow window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # Apply dropshadow to frame
        self.ui.central_widget_frame.setGraphicsEffect(self.shadow)

        # Maximize / Restore
        self.ui.maximize_button.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # Minimize
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())

        # Close
        self.ui.close_button.clicked.connect(lambda: self.close())

        # Create size grip to resize window
        self.sizegrip = QSizeGrip(self.ui.grip_frame)
        self.sizegrip.setStyleSheet(StyleSheet.get_resize_window_style())
        self.sizegrip.setToolTip("Resize Window")

    # Return status if windows is maximixe or restore
    def returnStatus():
        return GLOBAL_STATE
