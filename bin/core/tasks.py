import sqlite3
from navmanager import *
from filemanager import *
from export import *


class TaskManager():
	def __init__(self, tasks, logfilename="../../logs/tasklog.txt"):
		self.logfilename = logfilename
		open(self.logfilename, "a").write("\n\n**************\nNEW TASKS ADDED\n**************\n")
		self.tasklist = tasks
		print tasks
		self.results = []
		if os.path.exists("taskdb.db"):
			os.remove("taskdb.db")
			open(self.logfilename, "a").write("Existing data removed\n")
		self.conn = sqlite3.connect("taskdb2.db", isolation_level=None)
		self.conn.execute(
			'CREATE TABLE TASKS (task number, task_row number, task_column number, task_class TEXT, task_name TEXT, status TEXT)')
		self.conn.execute('CREATE TABLE INPUTS (task number, ipnum number, inplabel TEXT, value TEXT)')
		self.conn.execute('CREATE TABLE RESULTS (task number, link TEXT, html TEXT)')
		rows_for_tasks = []
		rows_for_inputs = []
		for i in self.tasklist:
			li = i[0:5]
			li.append("not started")
			rows_for_tasks.append(tuple(li))
			for j in i[5]:
				li = [i[0], j[0], j[1], j[2]]
				rows_for_inputs.append(tuple(li))
		self.conn.executemany('INSERT INTO TASKS VALUES (?,?,?,?,?,?)', rows_for_tasks)
		self.conn.executemany('INSERT INTO INPUTS VALUES (?,?,?,?)', rows_for_inputs)
		self.startAction()

	def startAction(self):
		for task in self.tasklist:
			self.updateStatus(task[0], "Task Initiated")
			if task[1] == 1:  # Navigation
				if task[2] == 0:  # Search Engine
					self.updateStatus(task[0], "Starting Search")
					n = self.searchengine(task)
					self.updateStatus(task[0], "Search Completed, [" + str(n) + "] results")
			break


	def searchengine(self, task):
		res = self.conn.execute('SELECT inplabel, value FROM INPUTS WHERE task=?', (task[0],))
		keyword, num, links = "", 1, False
		for i in res:
			if "Key" in i[0]:
				keyword = i[1]
			if "Num" in i[0]:
				num = i[1]
			if "links" in i[0]:
				links = True
			search = SearchEngine(keyword, num)
			res = search.search(links)
			n = 0
			for i in res:
				try:
					print task[0], i[0], i[1][0:100]
					self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)",
									  (task[0], i[0], unicode(i[1], 'utf-8', errors='replace')))
					n += 1
					if n>2:
						break
				except:
					open(self.logfilename, "a").write("Error Collecting data from " + i[0] + " \n")
			return n


	def updateStatus(self, tasknum, status):
		self.conn.execute('UPDATE TASKS SET status=? WHERE task=?', (status, tasknum))
		open(self.logfilename, "a").write("TASK[" + str(tasknum) + "]: " + status + "\n")
#
#
# if __name__ == '__main__':
# 	a = TaskManager([[0, 1, 0, 'Page Navigation', 'Search Engine', [[0, u'Keyword *', u'dsfgdf']]],
# 					 [1, 1, 0, 'Page Navigation', 'Search Engine',
# 					  [[0, u'Keyword *', u'cvbd'], [1, u'Number of Results', u'dfg']]],
# 					 [2, 1, 2, 'Page Navigation', 'URL list',
# 					  [[0, u'URL 1', u'dfg'], [1, u'URL 2', u'dfg'], [2, u'URL 3', u'dfg']]],
# 					 [3, 2, 0, 'Selection', 'HTML attributes', [[0, u'Tag', u'fdg']]]],
# 					logfilename="../logs/tasklog.txt")
# 	a.startAction()
#
