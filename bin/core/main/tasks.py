import os
import sqlite3


class TaskManager():
	def __init__(self, tasks):
		self.tasklist = tasks
		self.results = []
		if os.path.exists("taskdb.db"):
			os.remove("taskdb.db")
		self.conn = sqlite3.connect("taskdb.db", isolation_level=None)
		self.conn.execute('CREATE table TASKS (task number, task_row number, task_column number, status text)')
		self.conn.execute('CREATE table INPUTS (task number, ipnum number, link text, html text)')
		self.conn.execute('CREATE table RESULTS (task number, link text, html text)')
		for i in self.tasklist:
			pass

	def startAction(self):
		pass

	def saveLog(self, type, task, message):
		pass

