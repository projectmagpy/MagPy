import sqlite3
import urllib
import os


def create():
	if not os.path.exists("maindb.db"):
		conn = sqlite3.connect("maindb.db", isolation_level=None)
		c = conn.cursor()
		c.execute("""CREATE TABLE test (link TEXT, html TEXT, source TEXT)""")
	else:
		conn = sqlite3.connect("maindb.db", isolation_level=None)
	return conn


def createTasksDB():
	if os.path.exists("tasks.db"):
		os.remove("tasks.db")
	conn = sqlite3.connect("tasks.db", isolation_level=None)
	c = conn.cursor()
	c.execute('CREATE table TASKS (sl number, task_row number, task_column number, extern_index number, ' + \
			  'intern_index number, result_index number)')
	c.execute('CREATE table ARGS (sl number, task_row number, task_column number, ' + \
			  'a1 text, a2 text, a3 text, a4 text, a5 text)')
	c.execute('CREATE table RESULTS (sl number, task_row number, task_column number, ' + \
			  'link text, r2 text, r3 text)')
	return conn


if __name__ == '__main__':
	conn = createTasksDB()
	c = conn.cursor()
	x = ["Hello", "World"]
	c.execute('INSERT INTO TASKS VALUES (1, 1, 1, 1, 1, 1)')
	conn.close()