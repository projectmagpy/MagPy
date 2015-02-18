from PySide.QtGui import *
import guidata as data


class getInfo(QDialog):
	def __init__(self, item):
		super(getInfo, self).__init__()
		self.setModal(True)
		self.inputs = []
		self.item = item
		self.initUi()

	def initUi(self):
		l = QFormLayout()
		self.setLayout(l)

		self.type = data.tabHeadings.index(self.item[0])
		self.task = data.btns[self.type].index(self.item[1])

		if not len(data.inputs[self.type][self.task]) == 0:
			for i in data.inputs[self.type][self.task]:
				lab = QLabel(i)
				l.addWidget(lab)
				ip = QLineEdit()
				l.addWidget(ip)
				self.inputs.append([lab, ip])
			closebtn = QPushButton("Enter")
			l.addWidget(closebtn)
			closebtn.clicked.connect(self.close)

	def retval(self):
		return [[self.type, self.task, i[0].text(), i[1].text()] for i in self.inputs]

