# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created: Wed Apr 08 10:09:07 2015
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
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(209, 229, 255, 255), stop:1 rgba(37, 87, 146, 255));\n"
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
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.title_frame)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setContentsMargins(200, 10, 30, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtGui.QFrame(self.title_frame)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.title_image = QtGui.QFrame(self.title_frame)
        self.title_image.setAutoFillBackground(False)
        self.title_image.setStyleSheet("border-image: url(:/images/title.png);")
        self.title_image.setFrameShape(QtGui.QFrame.NoFrame)
        self.title_image.setFrameShadow(QtGui.QFrame.Plain)
        self.title_image.setObjectName("title_image")
        self.horizontalLayout_4.addWidget(self.title_image)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.title_frame)
        self.center_frame = QtGui.QFrame(self.base_frame)
        self.center_frame.setStyleSheet("")
        self.center_frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.center_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.center_frame.setLineWidth(2)
        self.center_frame.setObjectName("center_frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.center_frame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.startbtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.startbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.startbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.startbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.startbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/right39.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startbtn.setIcon(icon)
        self.startbtn.setIconSize(QtCore.QSize(50, 50))
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
        self.statusbtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.statusbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.statusbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/clipboard44.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statusbtn.setIcon(icon1)
        self.statusbtn.setIconSize(QtCore.QSize(50, 50))
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
        self.mvbtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.mvbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.mvbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mvbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mvbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/folder83.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mvbtn.setIcon(icon2)
        self.mvbtn.setIconSize(QtCore.QSize(50, 50))
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
        self.settingsbtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.settingsbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.settingsbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.settingsbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.settingsbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/document76.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsbtn.setIcon(icon3)
        self.settingsbtn.setIconSize(QtCore.QSize(50, 50))
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
        self.helpbtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.helpbtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.helpbtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.helpbtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.helpbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/lifebelt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpbtn.setIcon(icon4)
        self.helpbtn.setIconSize(QtCore.QSize(50, 50))
        self.helpbtn.setObjectName("helpbtn")
        self.verticalLayout_3.addWidget(self.helpbtn)
        self.horizontalLayout.addWidget(self.frame)
        self.mainTabs = QtGui.QStackedWidget(self.center_frame)
        self.mainTabs.setObjectName("mainTabs")
        self.MainUI = QtGui.QWidget()
        self.MainUI.setObjectName("MainUI")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.MainUI)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtGui.QFrame(self.MainUI)
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
        self.tasklist.setFrameShadow(QtGui.QFrame.Plain)
        self.tasklist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tasklist.setTabKeyNavigation(True)
        self.tasklist.setProperty("showDropIndicator", False)
        self.tasklist.setAlternatingRowColors(True)
        self.tasklist.setProperty("isWrapping", False)
        self.tasklist.setObjectName("tasklist")
        self.verticalLayout_4.addWidget(self.tasklist)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.MainUI)
        self.frame_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_3.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtGui.QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.filetab = QtGui.QWidget()
        self.filetab.setObjectName("filetab")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.filetab)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.filenavlist = QtGui.QListWidget(self.filetab)
        self.filenavlist.setObjectName("filenavlist")
        self.verticalLayout_7.addWidget(self.filenavlist)
        self.stackedWidget.addWidget(self.filetab)
        self.navtab = QtGui.QWidget()
        self.navtab.setObjectName("navtab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.navtab)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.navnavlist = QtGui.QListWidget(self.navtab)
        self.navnavlist.setObjectName("navnavlist")
        self.verticalLayout_8.addWidget(self.navnavlist)
        self.stackedWidget.addWidget(self.navtab)
        self.seltab = QtGui.QWidget()
        self.seltab.setObjectName("seltab")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.seltab)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selnavlist = QtGui.QListWidget(self.seltab)
        self.selnavlist.setFrameShape(QtGui.QFrame.NoFrame)
        self.selnavlist.setFrameShadow(QtGui.QFrame.Plain)
        self.selnavlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.selnavlist.setAutoScroll(False)
        self.selnavlist.setAutoScrollMargin(9)
        self.selnavlist.setAlternatingRowColors(True)
        self.selnavlist.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.selnavlist.setMovement(QtGui.QListView.Free)
        self.selnavlist.setResizeMode(QtGui.QListView.Fixed)
        self.selnavlist.setUniformItemSizes(True)
        self.selnavlist.setSelectionRectVisible(True)
        self.selnavlist.setObjectName("selnavlist")
        self.verticalLayout_6.addWidget(self.selnavlist)
        self.stackedWidget.addWidget(self.seltab)
        self.constraintstab = QtGui.QWidget()
        self.constraintstab.setObjectName("constraintstab")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.constraintstab)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.constraintlist = QtGui.QListWidget(self.constraintstab)
        self.constraintlist.setObjectName("constraintlist")
        self.verticalLayout_9.addWidget(self.constraintlist)
        self.stackedWidget.addWidget(self.constraintstab)
        self.exporttab = QtGui.QWidget()
        self.exporttab.setObjectName("exporttab")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.exporttab)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.exportnavlist = QtGui.QListWidget(self.exporttab)
        self.exportnavlist.setObjectName("exportnavlist")
        self.verticalLayout_10.addWidget(self.exportnavlist)
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
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prevbtn.setFont(font)
        self.prevbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.prevbtn.setFlat(True)
        self.prevbtn.setObjectName("prevbtn")
        self.horizontalLayout_3.addWidget(self.prevbtn)
        self.currentbtn = QtGui.QPushButton(self.frame_3)
        self.currentbtn.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentbtn.sizePolicy().hasHeightForWidth())
        self.currentbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.currentbtn.setFont(font)
        self.currentbtn.setStyleSheet("background-color: rgb(110, 110, 110);\n"
"color: rgb(224, 252, 255);")
        self.currentbtn.setFlat(True)
        self.currentbtn.setObjectName("currentbtn")
        self.horizontalLayout_3.addWidget(self.currentbtn)
        self.nextbtn = QtGui.QPushButton(self.frame_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextbtn.sizePolicy().hasHeightForWidth())
        self.nextbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextbtn.setFont(font)
        self.nextbtn.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.nextbtn.setFlat(True)
        self.nextbtn.setObjectName("nextbtn")
        self.horizontalLayout_3.addWidget(self.nextbtn)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.setStretch(0, 15)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.mainTabs.addWidget(self.MainUI)
        self.StatusPage = QtGui.QWidget()
        self.StatusPage.setObjectName("StatusPage")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.StatusPage)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_17 = QtGui.QFrame(self.StatusPage)
        self.frame_17.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_17.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.groupBox = QtGui.QGroupBox(self.frame_17)
        self.groupBox.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.prog_tot = QtGui.QProgressBar(self.groupBox)
        self.prog_tot.setProperty("value", 0)
        self.prog_tot.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.prog_tot.setTextVisible(True)
        self.prog_tot.setOrientation(QtCore.Qt.Horizontal)
        self.prog_tot.setInvertedAppearance(False)
        self.prog_tot.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.prog_tot.setObjectName("prog_tot")
        self.gridLayout_4.addWidget(self.prog_tot, 0, 1, 1, 1)
        self.prog_cur = QtGui.QProgressBar(self.groupBox)
        self.prog_cur.setProperty("value", 0)
        self.prog_cur.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.prog_cur.setTextVisible(True)
        self.prog_cur.setOrientation(QtCore.Qt.Horizontal)
        self.prog_cur.setInvertedAppearance(False)
        self.prog_cur.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.prog_cur.setObjectName("prog_cur")
        self.gridLayout_4.addWidget(self.prog_cur, 1, 1, 1, 1)
        self.verticalLayout_19.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame_17)
        self.groupBox_2.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)
        self.stat_ct = QtGui.QLabel(self.groupBox_2)
        self.stat_ct.setObjectName("stat_ct")
        self.gridLayout_5.addWidget(self.stat_ct, 1, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.stat_tk = QtGui.QLabel(self.groupBox_2)
        self.stat_tk.setObjectName("stat_tk")
        self.gridLayout_5.addWidget(self.stat_tk, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)
        self.stat_ti = QtGui.QLabel(self.groupBox_2)
        self.stat_ti.setObjectName("stat_ti")
        self.gridLayout_5.addWidget(self.stat_ti, 2, 1, 1, 1)
        self.verticalLayout_19.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.frame_17)
        self.groupBox_3.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.stat_pauseresumebtn = QtGui.QPushButton(self.groupBox_3)
        self.stat_pauseresumebtn.setObjectName("stat_pauseresumebtn")
        self.verticalLayout_20.addWidget(self.stat_pauseresumebtn)
        self.co_opensave = QtGui.QPushButton(self.groupBox_3)
        self.co_opensave.setObjectName("co_opensave")
        self.verticalLayout_20.addWidget(self.co_opensave)
        self.co_openlog = QtGui.QPushButton(self.groupBox_3)
        self.co_openlog.setObjectName("co_openlog")
        self.verticalLayout_20.addWidget(self.co_openlog)
        self.verticalLayout_19.addWidget(self.groupBox_3)
        self.horizontalLayout_6.addWidget(self.frame_17)
        self.frame_6 = QtGui.QFrame(self.StatusPage)
        self.frame_6.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.console = QtGui.QTextBrowser(self.frame_6)
        self.console.setProperty("cursor", QtCore.Qt.OpenHandCursor)
        self.console.setMouseTracking(True)
        self.console.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.console.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.console.setOpenExternalLinks(True)
        self.console.setObjectName("console")
        self.verticalLayout_12.addWidget(self.console)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtGui.QFrame(self.StatusPage)
        self.frame_7.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.clearbtn = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearbtn.sizePolicy().hasHeightForWidth())
        self.clearbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clearbtn.setFont(font)
        self.clearbtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.clearbtn.setObjectName("clearbtn")
        self.verticalLayout_11.addWidget(self.clearbtn)
        self.savebtn = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savebtn.sizePolicy().hasHeightForWidth())
        self.savebtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.savebtn.setFont(font)
        self.savebtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.savebtn.setObjectName("savebtn")
        self.verticalLayout_11.addWidget(self.savebtn)
        self.closebtn = QtGui.QPushButton(self.frame_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebtn.sizePolicy().hasHeightForWidth())
        self.closebtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.closebtn.setFont(font)
        self.closebtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.closebtn.setObjectName("closebtn")
        self.verticalLayout_11.addWidget(self.closebtn)
        self.horizontalLayout_6.addWidget(self.frame_7)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 5)
        self.horizontalLayout_6.setStretch(2, 1)
        self.mainTabs.addWidget(self.StatusPage)
        self.MyVault = QtGui.QWidget()
        self.MyVault.setObjectName("MyVault")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.MyVault)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_8 = QtGui.QFrame(self.MyVault)
        self.frame_8.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.frame_8)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame_8)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.username = QtGui.QLineEdit(self.frame_8)
        self.username.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.password = QtGui.QLineEdit(self.frame_8)
        self.password.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout)
        self.loginbtn = QtGui.QPushButton(self.frame_8)
        self.loginbtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.loginbtn.setObjectName("loginbtn")
        self.verticalLayout_14.addWidget(self.loginbtn)
        self.verticalLayout_13.addWidget(self.frame_8)
        self.frame_11 = QtGui.QFrame(self.MyVault)
        self.frame_11.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.loggedstatus = QtGui.QLabel(self.frame_11)
        self.loggedstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.loggedstatus.setObjectName("loggedstatus")
        self.horizontalLayout_11.addWidget(self.loggedstatus)
        self.verticalLayout_13.addWidget(self.frame_11)
        self.frame_10 = QtGui.QFrame(self.MyVault)
        self.frame_10.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.myvaultclearbtn = QtGui.QPushButton(self.frame_10)
        self.myvaultclearbtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.myvaultclearbtn.setObjectName("myvaultclearbtn")
        self.verticalLayout_21.addWidget(self.myvaultclearbtn)
        self.logoutbtn = QtGui.QPushButton(self.frame_10)
        self.logoutbtn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.logoutbtn.setObjectName("logoutbtn")
        self.verticalLayout_21.addWidget(self.logoutbtn)
        self.verticalLayout_13.addWidget(self.frame_10)
        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_13.setStretch(2, 3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.frame_9 = QtGui.QFrame(self.MyVault)
        self.frame_9.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.myvaultconsole = QtGui.QTextBrowser(self.frame_9)
        self.myvaultconsole.setObjectName("myvaultconsole")
        self.horizontalLayout_8.addWidget(self.myvaultconsole)
        self.horizontalLayout_7.addWidget(self.frame_9)
        self.mainTabs.addWidget(self.MyVault)
        self.SettingsPage = QtGui.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.SettingsPage)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_12 = QtGui.QFrame(self.SettingsPage)
        self.frame_12.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_5 = QtGui.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_5.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_18.addWidget(self.label_5)
        self.frame_15 = QtGui.QFrame(self.frame_12)
        self.frame_15.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.frame_15.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_15.setLineWidth(5)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ch_tl = QtGui.QPushButton(self.frame_15)
        self.ch_tl.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_tl.setObjectName("ch_tl")
        self.gridLayout_2.addWidget(self.ch_tl, 2, 2, 1, 1)
        self.ch_ml = QtGui.QPushButton(self.frame_15)
        self.ch_ml.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_ml.setObjectName("ch_ml")
        self.gridLayout_2.addWidget(self.ch_ml, 4, 2, 1, 1)
        self.ch_tn = QtGui.QPushButton(self.frame_15)
        self.ch_tn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_tn.setObjectName("ch_tn")
        self.gridLayout_2.addWidget(self.ch_tn, 5, 2, 1, 1)
        self.ch_ll = QtGui.QPushButton(self.frame_15)
        self.ch_ll.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_ll.setObjectName("ch_ll")
        self.gridLayout_2.addWidget(self.ch_ll, 3, 2, 1, 1)
        self.text_fl = QtGui.QLineEdit(self.frame_15)
        self.text_fl.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.text_fl.setObjectName("text_fl")
        self.gridLayout_2.addWidget(self.text_fl, 1, 1, 1, 1)
        self.text_tl = QtGui.QLineEdit(self.frame_15)
        self.text_tl.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.text_tl.setObjectName("text_tl")
        self.gridLayout_2.addWidget(self.text_tl, 2, 1, 1, 1)
        self.text_ml = QtGui.QLineEdit(self.frame_15)
        self.text_ml.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.text_ml.setObjectName("text_ml")
        self.gridLayout_2.addWidget(self.text_ml, 4, 1, 1, 1)
        self.text_ll = QtGui.QLineEdit(self.frame_15)
        self.text_ll.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.text_ll.setObjectName("text_ll")
        self.gridLayout_2.addWidget(self.text_ll, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_15)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_15)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_15)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame_15)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.text_tn = QtGui.QLineEdit(self.frame_15)
        self.text_tn.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.text_tn.setObjectName("text_tn")
        self.gridLayout_2.addWidget(self.text_tn, 5, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame_15)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.ch_fl = QtGui.QPushButton(self.frame_15)
        self.ch_fl.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_fl.setObjectName("ch_fl")
        self.gridLayout_2.addWidget(self.ch_fl, 1, 2, 1, 1)
        self.ch_re = QtGui.QPushButton(self.frame_15)
        self.ch_re.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.ch_re.setObjectName("ch_re")
        self.gridLayout_2.addWidget(self.ch_re, 6, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout_18.addWidget(self.frame_15)
        self.frame_16 = QtGui.QFrame(self.frame_12)
        self.frame_16.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.frame_16.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sp_seo = QtGui.QRadioButton(self.frame_16)
        self.sp_seo.setChecked(True)
        self.sp_seo.setObjectName("sp_seo")
        self.gridLayout_3.addWidget(self.sp_seo, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_16)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.sp_rec = QtGui.QRadioButton(self.frame_16)
        self.sp_rec.setObjectName("sp_rec")
        self.gridLayout_3.addWidget(self.sp_rec, 0, 2, 1, 1)
        self.verticalLayout_18.addWidget(self.frame_16)
        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 10)
        self.verticalLayout_15.addWidget(self.frame_12)
        self.mainTabs.addWidget(self.SettingsPage)
        self.HelpPage = QtGui.QWidget()
        self.HelpPage.setObjectName("HelpPage")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.HelpPage)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_13 = QtGui.QFrame(self.HelpPage)
        self.frame_13.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_13.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.textBrowser = QtGui.QTextBrowser(self.frame_13)
        self.textBrowser.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_17.addWidget(self.textBrowser)
        self.horizontalLayout_10.addWidget(self.frame_13)
        self.frame_14 = QtGui.QFrame(self.HelpPage)
        self.frame_14.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_14.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.textBrowser_2 = QtGui.QTextBrowser(self.frame_14)
        self.textBrowser_2.setStyleSheet("background-color: rgb(117, 117, 117);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_16.addWidget(self.textBrowser_2)
        self.horizontalLayout_10.addWidget(self.frame_14)
        self.mainTabs.addWidget(self.HelpPage)
        self.horizontalLayout.addWidget(self.mainTabs)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 7)
        self.verticalLayout_2.addWidget(self.center_frame)
        self.footer_frame = QtGui.QFrame(self.base_frame)
        self.footer_frame.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.footer_frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.footer_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.footer_frame.setLineWidth(2)
        self.footer_frame.setObjectName("footer_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addWidget(self.footer_frame)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.base_frame)

        self.retranslateUi(main_window)
        self.mainTabs.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "MagPy", None, QtGui.QApplication.UnicodeUTF8))
        self.startbtn.setText(QtGui.QApplication.translate("main_window", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.statusbtn.setText(QtGui.QApplication.translate("main_window", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.mvbtn.setText(QtGui.QApplication.translate("main_window", "MyVault", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsbtn.setText(QtGui.QApplication.translate("main_window", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.helpbtn.setText(QtGui.QApplication.translate("main_window", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.prevbtn.setText(QtGui.QApplication.translate("main_window", "File Management", None, QtGui.QApplication.UnicodeUTF8))
        self.currentbtn.setText(QtGui.QApplication.translate("main_window", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.nextbtn.setText(QtGui.QApplication.translate("main_window", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("main_window", "Progress", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("main_window", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("main_window", "Current Task", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("main_window", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("main_window", "Current task number", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_ct.setText(QtGui.QApplication.translate("main_window", "nil", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("main_window", "Number of tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_tk.setText(QtGui.QApplication.translate("main_window", "nil", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("main_window", "Time taken", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_ti.setText(QtGui.QApplication.translate("main_window", "nil", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("main_window", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_pauseresumebtn.setText(QtGui.QApplication.translate("main_window", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.co_opensave.setText(QtGui.QApplication.translate("main_window", "Open Saved location", None, QtGui.QApplication.UnicodeUTF8))
        self.co_openlog.setText(QtGui.QApplication.translate("main_window", "Open Log file", None, QtGui.QApplication.UnicodeUTF8))
        self.console.setHtml(QtGui.QApplication.translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Papyrus\'; font-size:8pt; font-style:italic;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearbtn.setText(QtGui.QApplication.translate("main_window", "Clear\n"
" Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.savebtn.setText(QtGui.QApplication.translate("main_window", "Save\n"
" Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.closebtn.setText(QtGui.QApplication.translate("main_window", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("main_window", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main_window", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.loginbtn.setText(QtGui.QApplication.translate("main_window", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.loggedstatus.setText(QtGui.QApplication.translate("main_window", "Not Logged in", None, QtGui.QApplication.UnicodeUTF8))
        self.myvaultclearbtn.setText(QtGui.QApplication.translate("main_window", "Clear Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.logoutbtn.setText(QtGui.QApplication.translate("main_window", "Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("main_window", "SETTINGS", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_tl.setText(QtGui.QApplication.translate("main_window", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_ml.setText(QtGui.QApplication.translate("main_window", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_tn.setText(QtGui.QApplication.translate("main_window", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_ll.setText(QtGui.QApplication.translate("main_window", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.text_fl.setText(QtGui.QApplication.translate("main_window", "../files/", None, QtGui.QApplication.UnicodeUTF8))
        self.text_tl.setText(QtGui.QApplication.translate("main_window", "../data.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.text_ml.setText(QtGui.QApplication.translate("main_window", "../files/", None, QtGui.QApplication.UnicodeUTF8))
        self.text_ll.setText(QtGui.QApplication.translate("main_window", "C://savedlog.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("main_window", "Files Output Location", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("main_window", "Text Output Location", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("main_window", "Logs Save Location", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("main_window", "MyVault Save Location", None, QtGui.QApplication.UnicodeUTF8))
        self.text_tn.setText(QtGui.QApplication.translate("main_window", "tasksdb.db", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("main_window", "Task database Name", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_fl.setText(QtGui.QApplication.translate("main_window", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.ch_re.setText(QtGui.QApplication.translate("main_window", "Reset All", None, QtGui.QApplication.UnicodeUTF8))
        self.sp_seo.setText(QtGui.QApplication.translate("main_window", "Position in search result", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("main_window", "Search Priority", None, QtGui.QApplication.UnicodeUTF8))
        self.sp_rec.setText(QtGui.QApplication.translate("main_window", "Most recurring links", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
