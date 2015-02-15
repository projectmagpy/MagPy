# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created: Mon Feb 16 02:22:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(900, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        main_window.setAutoFillBackground(False)
        main_window.setStyleSheet("QProgressBar:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    text-align: center;\n"
"    padding: 1px;\n"
"    background: #201F1F;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
"}\n"
"\n"
"QToolTip\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: rgb(90, 102, 117);;\n"
"    color: white;\n"
"    padding: 1px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: silver;\n"
"    background-color: #302F2F;\n"
"    selection-background-color:#78879b;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #78879b, stop: 1 #78879b);\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #78879b, stop: 1 #78879b);\n"
"}\n"
"\n"
"QMenuBar\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: silver;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #78879b;\n"
"    color: black;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #3A3939;\n"
"    color: silver;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::icon\n"
"{\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 5px 30px 5px 30px;\n"
"    margin-left: 5px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    alternate-background-color: #3A3939;\n"
"    color: silver;\n"
"    border: 1px solid 3A3939;\n"
"    border-radius: 3px;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QWidget:focus, QMenuBar:focus\n"
"{\n"
"    border: 1px solid rgba(48, 86, 111);\n"
"}\n"
"\n"
"QTabWidget:focus, QCheckBox:focus, QRadioButton:focus\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    padding: 2px;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 3px;\n"
"    color: silver;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border:1px solid #3A3939;\n"
"    border-radius: 7px;\n"
"    margin-top: 2ex;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 3px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 0px 11px 0px 11px;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 6px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,\n"
"    stop: 0 #302F2F, stop: 1 #484846);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,\n"
"    stop: 0 #605F5F, stop: 1 #787876);\n"
"    min-width: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,\n"
"    stop: 0 #302F2F, stop: 1 #484846);\n"
"    width: 15px;\n"
"    margin: 11px 0 11px 0;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0,\n"
"    stop: 0 #605F5F, stop: 1 #787876);\n"
"    min-height: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #201F1F;;\n"
"    color: silver;\n"
"    border-radius: 3px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"    color: #404040;\n"
"}\n"
"\n"
"QSizeGrip {\n"
"    image: url(:/qss_icons/rc/sizegrip.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: #302F2F;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #3A3939;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #58677b,\n"
"      stop:0.5 #78879b stop:1 #58677b);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #3A3939;\n"
"    spacing: 2px;\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #3A3939;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid silver;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"    cx: 0.5, cy: 0.5,\n"
"    fx: 0.5, fy: 0.5,\n"
"    radius: 1.0,\n"
"    stop: 0.25 #78879b,\n"
"    stop: 0.3 #302F2F\n"
"    );\n"
"}\n"
"\n"
"QCheckBox, QRadioButton\n"
"{\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #302F2F;\n"
"    border: 1px solid silver;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 7px;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/qss_icons/rc/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QStackedWidget\n"
"{\n"
"    border: none;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: 1px solid #393838;\n"
"    background: 1px solid #302F2F;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QToolBar::handle:horizontal {\n"
"    image: url(:/qss_icons/rc/Hmovetoolbar.png);\n"
"}\n"
"QToolBar::handle:vertical {\n"
"    image: url(:/qss_icons/rc/Vmovetoolbar.png);\n"
"}\n"
"QToolBar::separator:horizontal {\n"
"    image: url(:/qss_icons/rc/Hsepartoolbar.png);\n"
"}\n"
"QToolBar::separator:vertical {\n"
"    image: url(:/qss_icons/rc/Vsepartoolbars.png);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: silver;\n"
"    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0,\n"
"    stop: 0 #302F2F, stop: 1 #484846);\n"
"    border-width: 1px;\n"
"    border-color: #4A4949;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    border-radius: 5px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    border-width: 1px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 3px;*/\n"
"    color: #454545;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #78879b;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 3px;\n"
"    padding: 2px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    color: silver;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #626873;\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    selection-background-color: #4a4a4a;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #201F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid #3A3939;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0 #78879b, stop: 1 #78879b);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
"QComboBox::down-arrow:focus\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"    stop: 0 #302F2F, stop: 1 #484846);\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: #201F1F;\n"
"    color: silver;\n"
"    border-radius: 3px;\n"
"    min-width: 75px;\n"
"}\n"
"\n"
"QAbstractSpinBox:up-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center right;\n"
"}\n"
"\n"
"QAbstractSpinBox:down-button\n"
"{\n"
"    background-color: transparent;\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: center left;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
"    image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:hover\n"
"{\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QTabBar\n"
"{\n"
"    qproperty-drawBase: 0;\n"
"    padding-right: 15px;\n"
"}\n"
"\n"
"QTabBar:focus\n"
"{\n"
"    border: 0px transparent black;\n"
"}\n"
"\n"
"QTabBar::close-button  {\n"
"    image: url(:/qss_icons/rc/close.png);\n"
"    background: transparent;\n"
"    icon-size: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::close-button:hover\n"
"{\n"
"    background: rgba(255, 255, 255, 20);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::close-button:pressed {\n"
"    padding: 5px 4px 4px 5px;\n"
"}\n"
"\n"
"/* TOP - BOTTOM TABS */\n"
"QTabBar::tab:top {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,\n"
"      stop:1 #302F2F, stop:0 #5A5959);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,\n"
"      stop:1 #302F2F, stop:0 #5A5959);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"\n"
"    border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last\n"
"{\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:top:first:!selected, QTabBar::tab:bottom:first:!selected\n"
"{\n"
"    margin-left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    margin-top: 3px;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected\n"
"{\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    margin-bottom: 3px;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected\n"
"{\n"
"    margin-top: 0px;\n"
"}\n"
"\n"
"/* LEFT - RIGHT TABS */\n"
"QTabBar::tab:left {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: QLinearGradient(x1:1, y1:0, x2:0, y2:0,\n"
"      stop:1 #302F2F, stop:0 #5A5959);\n"
"    padding-left: 3px;\n"
"    padding-right: 2px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    margin-bottom: -1px;\n"
"\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #3A3939;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:1, y2:0,\n"
"      stop:1 #302F2F, stop:0 #5A5959);\n"
"    padding-left: 3px;\n"
"    padding-right: 2px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    margin-bottom: -1px;\n"
"\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    margin-right: 3px;\n"
"    background-color: #302F2F;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected\n"
"{\n"
"    margin-left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    margin-left: 3px;\n"
"        background-color: #302F2F;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected\n"
"{\n"
"    margin-right: 0px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/right_arrow.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:enabled {\n"
"     image: url(:/qss_icons/rc/left_arrow.png);\n"
" }\n"
"\n"
"QTabBar QToolButton::right-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
" }\n"
"\n"
" QTabBar QToolButton::left-arrow:disabled {\n"
"     image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
" }\n"
"\n"
"\n"
"QDockWidget {\n"
"    border: 1px solid #403F3F;\n"
"    titlebar-close-icon: url(:/qss_icons/rc/close.png);\n"
"    titlebar-normal-icon: url(:/qss_icons/rc/undock.png);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 3px;\n"
"    background: transparent;\n"
"    icon-size: 10px;\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
"    padding: 1px -1px -1px 1px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    border: 1px solid #78879b;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"QTreeView:branch:selected, QTreeView:branch:hover\n"
"{\n"
"    background: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/qss_icons/rc/transparent.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/qss_icons/rc/branch_closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"    image: url(:/qss_icons/rc/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
"QTreeView::branch:closed:has-children:has-siblings:hover {\n"
"    image: url(:/qss_icons/rc/branch_closed-on.png);\n"
"    }\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings:hover,\n"
"QTreeView::branch:open:has-children:has-siblings:hover  {\n"
"    image: url(:/qss_icons/rc/branch_open-on.png);\n"
"    }\n"
"\n"
"QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
"    background: rgba(0, 0, 0, 0);\n"
"    outline: 0;\n"
"    color: #FFFFFF\n"
"}\n"
"\n"
"QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
"    background: #78879b;;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 3px;\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QToolButton:pressed, QToolButton::menu-button:pressed {\n"
"    background-color: #4A4949;\n"
"    border: 1px solid silver;\n"
"}\n"
"\n"
"QToolButton:hover, QToolButton::menu-button:hover {\n"
"    background-color: #4A4949;\n"
"    border: 1px solid gray;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
" padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton[popupMode=\"2\"] { /* only for MenuButtonPopup */\n"
" padding-right: 10px; /* make way for the popup button */\n"
"}\n"
"\n"
"/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
"QToolButton::menu-button {\n"
" border: 1px solid #3A3939;\n"
" border-top-right-radius: 6px;\n"
" border-bottom-right-radius: 6px;\n"
" /* 16px width + 4px for border = 20px allocated above */\n"
" width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
" image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QToolButton::menu-arrow:open {\n"
" top: 1px; left: 1px; /* shift it a bit */\n"
"}\n"
"\n"
"QPushButton::menu-indicator  {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    left: 8px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    border: transparent;\n"
"    gridline-color: #6c6c6c;\n"
"    background-color: #201F1F;\n"
"}\n"
"\n"
"\n"
"QTableView, QHeaderView\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {\n"
"    background: #78879b;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QHeaderView\n"
"{\n"
"    border: 1px transparent;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section  {\n"
"    background-color: #3A3939;\n"
"    color: silver;\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    border-radius: 0px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: transparent;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QHeaderView::section::horizontal\n"
"{\n"
"    border-left: transparent;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
" {\n"
"    color: white;\n"
"    background-color: #5A5959;\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
"QHeaderView::down-arrow {\n"
"    image: url(:/qss_icons/rc/down_arrow.png);\n"
"}\n"
"\n"
"QHeaderView::up-arrow {\n"
"    image: url(:/qss_icons/rc/up_arrow.png);\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #3A3939;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:1 #302F2F, stop:0 #5A5959);\n"
"    width: 100%;\n"
"    padding-left: 3px;\n"
"    padding-right: 2px;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    margin-bottom: -1px;\n"
"\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    color: darkgray;\n"
" }\n"
"\n"
" QToolBox::tab:selected { /* italicize selected tabs */\n"
"     font: italic bold;\n"
"     color: white;\n"
" }\n"
"\n"
"QStatusBar::item {\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 3px;\n"
" }")
        main_window.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(main_window)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.base_frame = QtGui.QFrame(main_window)
        self.base_frame.setFrameShape(QtGui.QFrame.Box)
        self.base_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.base_frame.setObjectName("base_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.base_frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_frame = QtGui.QFrame(self.base_frame)
        self.title_frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.title_frame.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.title_frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.title_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.title_frame.setLineWidth(2)
        self.title_frame.setMidLineWidth(1)
        self.title_frame.setObjectName("title_frame")
        self.verticalLayout_2.addWidget(self.title_frame)
        self.center_frame = QtGui.QFrame(self.base_frame)
        self.center_frame.setStyleSheet("")
        self.center_frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.center_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.center_frame.setLineWidth(2)
        self.center_frame.setObjectName("center_frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.center_frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(self.center_frame)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startbtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.startbtn.setFont(font)
        self.startbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.startbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.startbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.startbtn.setObjectName("startbtn")
        self.verticalLayout_3.addWidget(self.startbtn)
        self.statusbtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbtn.sizePolicy().hasHeightForWidth())
        self.statusbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.statusbtn.setFont(font)
        self.statusbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.statusbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.statusbtn.setObjectName("statusbtn")
        self.verticalLayout_3.addWidget(self.statusbtn)
        self.mvbtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mvbtn.sizePolicy().hasHeightForWidth())
        self.mvbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.mvbtn.setFont(font)
        self.mvbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mvbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mvbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.mvbtn.setObjectName("mvbtn")
        self.verticalLayout_3.addWidget(self.mvbtn)
        self.settingsbtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsbtn.sizePolicy().hasHeightForWidth())
        self.settingsbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.settingsbtn.setFont(font)
        self.settingsbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.settingsbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.settingsbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.settingsbtn.setObjectName("settingsbtn")
        self.verticalLayout_3.addWidget(self.settingsbtn)
        self.helpbtn = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpbtn.sizePolicy().hasHeightForWidth())
        self.helpbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.helpbtn.setFont(font)
        self.helpbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.helpbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.helpbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.helpbtn.setObjectName("helpbtn")
        self.verticalLayout_3.addWidget(self.helpbtn)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.center_frame)
        self.frame_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_2.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tasklist = QtGui.QListWidget(self.frame_2)
        self.tasklist.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tasklist.setFrameShape(QtGui.QFrame.NoFrame)
        self.tasklist.setFrameShadow(QtGui.QFrame.Sunken)
        self.tasklist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tasklist.setTabKeyNavigation(True)
        self.tasklist.setProperty("showDropIndicator", False)
        self.tasklist.setAlternatingRowColors(True)
        self.tasklist.setProperty("isWrapping", False)
        self.tasklist.setObjectName("tasklist")
        self.verticalLayout_4.addWidget(self.tasklist)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.center_frame)
        self.frame_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_3.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtGui.QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.filetab = QtGui.QWidget()
        self.filetab.setObjectName("filetab")
        self.label_3 = QtGui.QLabel(self.filetab)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 46, 13))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.filetab)
        self.navtab = QtGui.QWidget()
        self.navtab.setObjectName("navtab")
        self.label_4 = QtGui.QLabel(self.navtab)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 46, 13))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.navtab)
        self.seltab = QtGui.QWidget()
        self.seltab.setObjectName("seltab")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.seltab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selnav = QtGui.QListWidget(self.seltab)
        self.selnav.setObjectName("selnav")
        self.verticalLayout_6.addWidget(self.selnav)
        self.stackedWidget.addWidget(self.seltab)
        self.widget = QtGui.QWidget()
        self.widget.setObjectName("widget")
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(70, 100, 46, 13))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.widget)
        self.exporttab = QtGui.QWidget()
        self.exporttab.setObjectName("exporttab")
        self.label_2 = QtGui.QLabel(self.exporttab)
        self.label_2.setGeometry(QtCore.QRect(310, 360, 46, 13))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.exporttab)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.prevbtn = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevbtn.sizePolicy().hasHeightForWidth())
        self.prevbtn.setSizePolicy(sizePolicy)
        self.prevbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.prevbtn.setObjectName("prevbtn")
        self.horizontalLayout_3.addWidget(self.prevbtn)
        self.currentbtn = QtGui.QPushButton(self.frame_3)
        self.currentbtn.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentbtn.sizePolicy().hasHeightForWidth())
        self.currentbtn.setSizePolicy(sizePolicy)
        self.currentbtn.setStyleSheet("background-color: rgb(110, 110, 110);\n"
"color: rgb(224, 252, 255);")
        self.currentbtn.setFlat(False)
        self.currentbtn.setObjectName("currentbtn")
        self.horizontalLayout_3.addWidget(self.currentbtn)
        self.nextbtn = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextbtn.sizePolicy().hasHeightForWidth())
        self.nextbtn.setSizePolicy(sizePolicy)
        self.nextbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.nextbtn.setObjectName("nextbtn")
        self.horizontalLayout_3.addWidget(self.nextbtn)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.setStretch(0, 6)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.frame_3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout_2.addWidget(self.center_frame)
        self.footer_frame = QtGui.QFrame(self.base_frame)
        self.footer_frame.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.footer_frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.footer_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.footer_frame.setLineWidth(2)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtGui.QFrame(self.footer_frame)
        self.frame_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.closebtn = QtGui.QPushButton(self.footer_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebtn.sizePolicy().hasHeightForWidth())
        self.closebtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.closebtn.setFont(font)
        self.closebtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.closebtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.closebtn.setObjectName("closebtn")
        self.horizontalLayout_2.addWidget(self.closebtn)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.footer_frame)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 7)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.base_frame)

        self.retranslateUi(main_window)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "MagPy", None, QtGui.QApplication.UnicodeUTF8))
        self.startbtn.setText(QtGui.QApplication.translate("main_window", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbtn.setText(QtGui.QApplication.translate("main_window", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.mvbtn.setText(QtGui.QApplication.translate("main_window", "MyVault", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsbtn.setText(QtGui.QApplication.translate("main_window", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.helpbtn.setText(QtGui.QApplication.translate("main_window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("main_window", "hgjophjkl", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("main_window", "56jr56j", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main_window", "asdgfasdg", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("main_window", "asdgfasdg", None, QtGui.QApplication.UnicodeUTF8))
        self.prevbtn.setText(QtGui.QApplication.translate("main_window", "File Management", None, QtGui.QApplication.UnicodeUTF8))
        self.currentbtn.setText(QtGui.QApplication.translate("main_window", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.nextbtn.setText(QtGui.QApplication.translate("main_window", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.closebtn.setText(QtGui.QApplication.translate("main_window", "Close", None, QtGui.QApplication.UnicodeUTF8))

