from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


from .style_sheet import StyleSheet


class MainWindowUi(object):
    def setup_ui(self, MainWindow):
        # Set MainWindow
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setMinimumSize(QSize(880, 600))

        # Set central_widget
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")

        # Set vertical layout for central_widget
        self.central_widget_vertical_layout = QVBoxLayout(self.central_widget)
        self.central_widget_vertical_layout.setObjectName(u"central_widget_vertical_layout")

        # Set central_widget_frame
        self.central_widget_frame = QFrame(self.central_widget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setStyleSheet(StyleSheet.get_central_widget_frame_style())

        # Set vertical layout for central_widget_frame
        self.central_widget_frame_vertical_layout = QVBoxLayout(self.central_widget_frame)
        self.central_widget_frame_vertical_layout.setSpacing(0)
        self.central_widget_frame_vertical_layout.setObjectName(u"central_widget_frame_vertical_layout")
        self.central_widget_frame_vertical_layout.setContentsMargins(0, 0, 0, 0)

        # Set title_bar_frame
        self.title_bar_frame = QFrame(self.central_widget_frame)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setMaximumSize(QSize(16777215, 30))
        self.title_bar_frame.setStyleSheet(StyleSheet.get_title_bar_frame_style())
        self.title_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.title_bar_frame.setFrameShadow(QFrame.Raised)

        # Set horizontal layout for title_bar_frame
        self.title_bar_frame_horizontal_layout = QHBoxLayout(self.title_bar_frame)
        self.title_bar_frame_horizontal_layout.setObjectName(u"title_bar_frame_horizontal_layout")
        self.title_bar_frame_horizontal_layout.setContentsMargins(15, 0, 0, 0)
        self.title_bar_frame_horizontal_layout.setSpacing(0)

        # Set menu_frame
        self.menu_frame = QFrame(self.title_bar_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(180, 16777215))
        self.menu_frame.setMaximumSize(QSize(180, 16777215))
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Plain)

        # Set horizontal layout for menu_frame
        self.menu_frame_horizontal_layout = QHBoxLayout(self.menu_frame)
        self.menu_frame_horizontal_layout.setObjectName(u"menu_frame_horizontal_layout")
        self.menu_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame_horizontal_layout.setSpacing(0)

        # Set logo lebel
        self.logo_label = QLabel(self.menu_frame)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(30, 16777215))
        self.logo_label.setMaximumSize(QSize(30, 16777215))
        self.logo_label.setText(u"")
        self.logo_label.setPixmap(QPixmap(u"icons/window_logo.png"))

        self.menu_frame_horizontal_layout.addWidget(self.logo_label)

        # Set menu bar
        self.file_button = QPushButton(self.menu_frame)
        self.file_button.setObjectName(u"file_button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_button.sizePolicy().hasHeightForWidth())
        self.file_button.setSizePolicy(sizePolicy)
        self.file_button.setMinimumSize(QSize(50, 16777215))
        self.file_button.setMaximumSize(QSize(50, 16777215))

        menu_bar_font = QFont()
        menu_bar_font.setFamily(u"Roboto")
        menu_bar_font.setPointSize(10)
        self.file_button.setFont(menu_bar_font)
        self.file_button.setStyleSheet(StyleSheet.get_menu_bar_style())

        self.menu_frame_horizontal_layout.addWidget(self.file_button)

        self.tools_button = QPushButton(self.menu_frame)
        self.file_button.setObjectName(u"tools_button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_button.sizePolicy().hasHeightForWidth())
        self.tools_button.setSizePolicy(sizePolicy)
        self.tools_button.setMinimumSize(QSize(50, 16777215))
        self.tools_button.setMaximumSize(QSize(50, 16777215))
        self.tools_button.setFont(menu_bar_font)
        self.tools_button.setStyleSheet(StyleSheet.get_menu_bar_style())

        self.menu_frame_horizontal_layout.addWidget(self.tools_button)

        self.help_button = QPushButton(self.menu_frame)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy)
        self.help_button.setMinimumSize(QSize(50, 16777215))
        self.help_button.setMaximumSize(QSize(50, 16777215))
        self.help_button.setFont(menu_bar_font)
        self.help_button.setStyleSheet(StyleSheet.get_menu_bar_style())

        self.menu_frame_horizontal_layout.addWidget(self.help_button)
        self.title_bar_frame_horizontal_layout.addWidget(self.menu_frame)

        # Set title_frame
        self.title_frame = QFrame(self.title_bar_frame)
        self.title_frame.setObjectName(u"title_frame")

        # Set horizontal layout for title_frame
        self.title_frame_horizontal_layout = QHBoxLayout(self.title_frame)
        self.title_frame_horizontal_layout.setObjectName(u"title_frame_horizontal_layout")
        self.title_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.title_frame_horizontal_layout.setSpacing(0)

        # Set title label
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font =  QFont()
        title_font.setFamily(u"Roboto")
        title_font.setPointSize(10)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet(StyleSheet.get_title_label_style())

        self.title_frame_horizontal_layout.addWidget(self.title_label)
        self.title_bar_frame_horizontal_layout.addWidget(self.title_frame)
        
        # Set frame for buttons
        self.buttons_frame = QFrame(self.title_bar_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(150, 30))
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Plain)
        self.buttons_frame.setLineWidth(0)

        # Set horizontal Layout for buttons_frame
        self.buttons_frame_horizontal_layout = QHBoxLayout(self.buttons_frame)
        self.buttons_frame_horizontal_layout.setObjectName(u"buttons_frame_horizontal_layout")
        self.buttons_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_frame_horizontal_layout.setSpacing(0)

        # Set minimize_button
        self.minimize_button = QPushButton(self.buttons_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMaximumSize(QSize(50, 30))
        self.minimize_button.setStyleSheet(StyleSheet.get_mimimize_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/hide.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap("icons/hide_active.png"), QIcon.Normal, QIcon.On)
        self.minimize_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.minimize_button)

        # Set maximize_button
        self.maximize_button = QPushButton(self.buttons_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMaximumSize(QSize(50, 30))
        self.maximize_button.setStyleSheet(StyleSheet.get_maximize_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/maximize.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap("icons/maximize_active.png"), QIcon.Normal, QIcon.On)
        self.maximize_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.maximize_button)

        # Set close_button
        self.close_button = QPushButton(self.buttons_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMaximumSize(QSize(50, 30))
        self.close_button.setStyleSheet(StyleSheet.get_close_button_style())

        icon = QIcon()
        icon.addPixmap(QPixmap("icons/close_active.png"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap("icons/close_active.png"), QIcon.Normal, QIcon.On)
        icon.addPixmap(QPixmap("icons/close_active.png"), QIcon.Selected, QIcon.On)
        self.close_button.setIcon(icon)

        self.buttons_frame_horizontal_layout.addWidget(self.close_button)
        self.title_bar_frame_horizontal_layout.addWidget(self.buttons_frame)
        self.central_widget_frame_vertical_layout.addWidget(self.title_bar_frame)

        # Set content_bar_frame
        self.content_bar_frame = QFrame(self.central_widget_frame)
        self.content_bar_frame.setObjectName(u"content_bar_frame")
        self.content_bar_frame.setStyleSheet(StyleSheet.get_content_bar_frame_style())
        self.content_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.content_bar_frame.setFrameShadow(QFrame.Raised)

        # Set vertical layout for content_bar_frame
        self.content_bar_frame_vertical_layout = QVBoxLayout(self.content_bar_frame)
        self.content_bar_frame_vertical_layout.setObjectName(u"content_bar_frame_vertical_layout")

        self.central_widget_frame_vertical_layout.addWidget(self.content_bar_frame)

        # Set credit_bar_frame
        self.credit_bar_frame = QFrame(self.central_widget_frame)
        self.credit_bar_frame.setObjectName(u"credit_bar_frame")
        self.credit_bar_frame.setMaximumSize(QSize(16777215, 30))
        self.credit_bar_frame.setStyleSheet(StyleSheet.get_credit_bar_frame_style())
        self.credit_bar_frame.setFrameShape(QFrame.NoFrame)
        self.credit_bar_frame.setFrameShadow(QFrame.Raised)

        # Set horizontal layout for credit_bar_frame
        self.credit_bar_frame_horizontal_layout = QHBoxLayout(self.credit_bar_frame)
        self.credit_bar_frame_horizontal_layout.setSpacing(0)
        self.credit_bar_frame_horizontal_layout.setObjectName(u"credit_bar_frame_horizontal_layout")
        self.credit_bar_frame_horizontal_layout.setContentsMargins(0, 0, 0, 0)

        # Set credit_bar_label_frame
        self.credit_bar_label_frame = QFrame(self.credit_bar_frame)
        self.credit_bar_label_frame.setObjectName(u"credit_bar_label_frame")
        self.credit_bar_label_frame.setFrameShape(QFrame.StyledPanel)
        self.credit_bar_label_frame.setFrameShadow(QFrame.Raised)

        # Set vertical layout for credit_bar_label_frame
        self.credit_bar_label_frame_vertical_layout = QVBoxLayout(self.credit_bar_label_frame)
        self.credit_bar_label_frame_vertical_layout.setSpacing(0)
        self.credit_bar_label_frame_vertical_layout.setObjectName(u"credit_bar_label_frame_vertical_layout")
        self.credit_bar_label_frame_vertical_layout.setContentsMargins(15, 0, 0, 0)

        # Set label on credit_bar_label_frame
        self.credits_label = QLabel(self.credit_bar_label_frame)
        self.credits_label.setObjectName(u"credits_label")
        credits_label_font = QFont()
        credits_label_font.setFamily(u"Roboto")
        self.credits_label.setFont(credits_label_font)
        self.credits_label.setStyleSheet(StyleSheet.get_credits_label_style())

        self.credit_bar_label_frame_vertical_layout.addWidget(self.credits_label)
        self.credit_bar_frame_horizontal_layout.addWidget(self.credit_bar_label_frame)

        # Set grip_frame
        self.grip_frame = QFrame(self.credit_bar_frame)
        self.grip_frame.setObjectName(u"grip_frame")
        self.grip_frame.setMinimumSize(QSize(30, 30))
        self.grip_frame.setMaximumSize(QSize(30, 30))
        self.grip_frame.setStyleSheet(StyleSheet.get_grip_frame_style())
        self.grip_frame.setFrameShape(QFrame.StyledPanel)
        self.grip_frame.setFrameShadow(QFrame.Raised)

        self.credit_bar_frame_horizontal_layout.addWidget(self.grip_frame)
        self.central_widget_frame_vertical_layout.addWidget(self.credit_bar_frame)
        self.central_widget_vertical_layout.addWidget(self.central_widget_frame)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate('MainWindow', u'MainWindow', None))
        self.title_label.setText(QCoreApplication.translate('MainWindow', u'MILT.DICOM', None))
        self.file_button.setText(QCoreApplication.translate('MainWindow', u'   File', None))
        self.tools_button.setText(QCoreApplication.translate('MainWindow', u'   Tools', None))
        self.help_button.setText(QCoreApplication.translate('MainWindow', u'   Help', None))
        self.maximize_button.setToolTip(QCoreApplication.translate('MainWindow', u'Maximize', None))
        self.credits_label.setText(QCoreApplication.translate('MainWindow', u'Designed by: Daria Tsvetkova. Developed by Alexey Popov. February 2022', None))
