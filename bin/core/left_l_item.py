# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left_l_item.ui'
#
# Created: Mon Mar 16 00:21:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(911, 377)
        Frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.48, y1:0, x2:0.486, y2:0.517045, stop:0.0621469 rgba(103, 103, 103, 255), stop:1 rgba(193, 193, 193, 255));")
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Plain)
        self.horizontalLayout = QtGui.QHBoxLayout(Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(Frame)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(86, 86, 86)")
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.type = QtGui.QLabel(self.frame_3)
        self.type.setStyleSheet("color: rgb(255, 255, 255);")
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setStyleSheet("background-color: rgb(110, 110, 110);\n"
"color: rgb(224, 252, 255);")
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.desc = QtGui.QLabel(self.frame_5)
        self.desc.setObjectName("desc")
        self.verticalLayout_3.addWidget(self.desc)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.setStretch(0, 500)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2000)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(Frame)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.gridlayout = QtGui.QGridLayout(self.frame_2)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/undo6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridlayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.itemCloseBtn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemCloseBtn.sizePolicy().hasHeightForWidth())
        self.itemCloseBtn.setSizePolicy(sizePolicy)
        self.itemCloseBtn.setAutoFillBackground(False)
        self.itemCloseBtn.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.itemCloseBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/delete30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemCloseBtn.setIcon(icon1)
        self.itemCloseBtn.setIconSize(QtCore.QSize(30, 30))
        self.itemCloseBtn.setDefault(False)
        self.itemCloseBtn.setFlat(False)
        self.itemCloseBtn.setObjectName("itemCloseBtn")
        self.gridlayout.addWidget(self.itemCloseBtn, 0, 1, 1, 1)
        self.itemUpBtn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemUpBtn.sizePolicy().hasHeightForWidth())
        self.itemUpBtn.setSizePolicy(sizePolicy)
        self.itemUpBtn.setAutoFillBackground(False)
        self.itemUpBtn.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.itemUpBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/navigate3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemUpBtn.setIcon(icon2)
        self.itemUpBtn.setIconSize(QtCore.QSize(30, 30))
        self.itemUpBtn.setDefault(False)
        self.itemUpBtn.setFlat(False)
        self.itemUpBtn.setObjectName("itemUpBtn")
        self.gridlayout.addWidget(self.itemUpBtn, 1, 0, 1, 1)
        self.itemDwnBtn = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemDwnBtn.sizePolicy().hasHeightForWidth())
        self.itemDwnBtn.setSizePolicy(sizePolicy)
        self.itemDwnBtn.setAutoFillBackground(False)
        self.itemDwnBtn.setStyleSheet("background-color: rgb(98, 98, 98);")
        self.itemDwnBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/navigate2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemDwnBtn.setIcon(icon3)
        self.itemDwnBtn.setIconSize(QtCore.QSize(30, 30))
        self.itemDwnBtn.setDefault(False)
        self.itemDwnBtn.setFlat(False)
        self.itemDwnBtn.setObjectName("itemDwnBtn")
        self.gridlayout.addWidget(self.itemDwnBtn, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.type.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.desc.setText(QtGui.QApplication.translate("Frame", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
