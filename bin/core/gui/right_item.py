from PySide.QtGui import QFrame
import right_l_item, qdarkstyle

class Item(QFrame, right_l_item.Ui_Frame):
	"""
	A Class that handles the interactions between the GUI and the program. The GUI file [gui.py] is to be imported
	and handled here. All Signal Slot interactions are handled by this class.

	1. collecting keywords
	2. collecting all constraints
	3. voice based interactions
	4. display results
	5. options to export data, settings, etc.


	Class handled by Paul Jacob
	"""

	def __init__(self):
		super(Item, self).__init__()
		self.setupUi(self)
		# self.setStyleSheet(qdarkstyle.load_stylesheet())