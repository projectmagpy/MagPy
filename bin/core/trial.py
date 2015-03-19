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


if __name__ == '__main__':
    conn = createTasksDB()
    c = conn.cursor()

    # list of url's

    # urls = ["http://wikipedia.org", "http://www.marutisuzuki.com/swift.aspx"]
    # data = n.basicnav().listnav(["http://wikipedia.org", "http://www.marutisuzuki.com/swift.aspx"])
    # for url in urls:
    #     print url
    #     da = data[urls.index(url)][0][1]
    #     c.execute('INSERT INTO RESULT (link, html) VALUES (?, ?)', (url, da))

    #single url

    # url = "http://en.wikipedia.org/wiki/BMW_i8"
    # data = n.basicnav().single("http://en.wikipedia.org/wiki/BMW_i8")[1]
    # c.execute('INSERT INTO RESULT VALUES (?,?)', (url, data))

    #iterative url

    url = "http://forum.xda-developers.com/showthread.php?t=779%d1"
    data = n.basicnav().iterativenav("http://forum.xda-developers.com/showthread.php?t=779%d1",'num',100,103)
    x = []
    for i in data:
        x.append((i[0], i[1]))
    c.executemany('INSERT INTO RESULT VALUES (?,?)', x)
    conn.close()
