from PySide.QtCore import Qt
from PySide.QtGui import *
import sys
import qdarkstyle

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(qdarkstyle.load_stylesheet())

app = QApplication(sys.argv)
ap = MyApp()
ap.show()
app.exec_()