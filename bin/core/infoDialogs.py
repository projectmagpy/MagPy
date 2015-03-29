from PySide.QtGui import *
from PySide.QtCore import *
import guidata as data


class getInfo(QDialog):
    def __init__(self, item):
        super(getInfo, self).__init__()
        self.setModal(True)
        self.inputs = []
        self.item = item
        self.setWindowTitle("Enter Data")
        self.initUi()

    def initUi(self):
        l = QFormLayout()
        self.setLayout(l)

        self.type = data.tabHeadings.index(self.item[0])
        self.task = data.btns[self.type].index(self.item[1])
        self.num_ip = len(data.inputs[self.type][self.task])

        if not len(data.inputs[self.type][self.task]) == 0:
            for i in data.inputs[self.type][self.task]:
                lab = QLabel(i)
                l.addWidget(lab)
                ip = QLineEdit()
                l.addWidget(ip)
                ip.textChanged.connect(self.changeButtonText)
                self.inputs.append([lab, ip])
            self.closebtn = QPushButton("Close")
            l.addWidget(self.closebtn)
            self.closebtn.clicked.connect(self.close)
        else:
            self.retval()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def changeButtonText(self, txt):
        if len(txt) > 0:
            self.closebtn.setText("Add this task")
        else:
            self.closebtn.setText("Close")

    def retval(self):
        res = []
        for i in self.inputs:
            if len(i[1].text()) > 0:
                res.append([self.type, self.task, i[0].text(), i[1].text()])
        if len(res) != 0:
            return res
        elif len(self.inputs) == 0:
            return [[self.type, self.task, "NULLTXT"]]

