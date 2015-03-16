import navmanager as n
import sqlite3
import urllib
import os

def create():
    if not os.path.exists("maindb.db"):
        conn = sqlite3.connect("maindb.db", isolation_level=None)
        c = conn.cursor()
        c.execute("""CREATE TABLE test (link TEXT, html TEXT)""")
    else:
        conn = sqlite3.connect("maindb.db", isolation_level=None)
    return conn

def createTasksDB():
    if os.path.exists("tasks2.db"):
        os.remove("tasks2.db")
    conn = sqlite3.connect("tasks2.db", isolation_level=None)
    c = conn.cursor()
    c.execute('CREATE table RESULT (link VARCHAR2, html VARCHAR2)')
    return conn

if __name__=='__main__':
    conn = createTasksDB()
    c = conn.cursor()
    #urls = ["http://wikipedia.org", "http://www.marutisuzuki.com/swift.aspx"]
    #data = n.basicnav().listnav(["http://wikipedia.org", "http://www.marutisuzuki.com/swift.aspx"])
    #for url in urls:
    #    print url
    c.execute('INSERT INTO RESULT (link, html) VALUES ("http://wikipedia.org", 1)')
    conn.close()