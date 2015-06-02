from PySide.QtGui import *
import right_l_item


class Item(QFrame, right_l_item.Ui_Frame):
    def __init__(self):
        super(Item, self).__init__()
        self.setupUi(self)

    def initUi(self):
        pass

    def updateUi(self):
        pass