import sqlite3
from navmanager import *
from filemanager import *
from export import *
import constants


class TaskManager():
    def __init__(self, tasks, logfilename=constants.tasklog):
        self.logfilename = logfilename
        open(self.logfilename, "a").write("\n\n**************\nNEW TASKS ADDED\n**************\n")
        self.tasklist = tasks
        print tasks
        self.results = []
        if os.path.exists(constants.taskdbloc):
            os.remove(constants.taskdbloc)
            open(self.logfilename, "a").write("Existing data removed\n")
        self.conn = sqlite3.connect(constants.taskdbloc, isolation_level=None)
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
        self.funcs = [self.file, self.navmgr, self.select, self.constrain, self.export]
        self.updateStatus(self.tasklist[0][0], "Task Initiated")
        self.funcs[self.tasklist[0][1]](0)

    def select(self, tnum):
        task = self.tasklist[tnum]
        if task[2] == 0:  # HTML attributes
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["", "", ""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            b = BeautifulSoup(html)
            if ips[2] != "":
                r1 = b.find(ips[0], attrs={"id": ips[2]})
            else:
                r1 = " :: ".join(b.findAll(ips[0]))

            self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, " ", unicode(r1, errors="ignore")))

        if task[2] == 3:  # From Text
            pass
        if task[2] == 4:  # Regular Expressions
            pass

        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)



    def constrain(self, task):
        pass


    def export(self, task):
        pass


    def file(self, tnum):
        task = self.tasklist[tnum]
        if task[2] == 0:  # text
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
                b = BeautifulSoup(html)
                data = "\n".join(i.text for i in b.findAll("p"))
            else:
                html = requests.get(ips[0])
                b = BeautifulSoup(html)
                data = "\n".join(i.text for i in b.findAll("p"))
            open(constants.textop, "w").write(data)

        if task[2] == 1:  # images
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
            else:
                html = requests.get(ips[0])
            b = BeautifulSoup(html)
            for im in b.findAll("img"):
                urllib.urlopen(im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])

        if task[2] == 2:  # videos
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
            else:
                html = requests.get(ips[0])
            b = BeautifulSoup(html)
            for im in b.findAll("a"):
                if "mp4" in im["href"]:
                    urllib.urlopen(im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])

        if task[2] == 3:  # files
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
            else:
                html = requests.get(ips[0])
            b = BeautifulSoup(html)
            for im in b.findAll("a"):
                if "pdf" in im["href"]:
                    urllib.urlopen(im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])

        if task[2] == 4:  # html
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
            else:
                html = requests.get(ips[0])
            open(constants.fileloc + "op.html", "w").write(html)

        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)

    def navmgr(self, tnum):
        task = self.tasklist[tnum]
        if task[2] == 0:  # Search Engine
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["none", "1", "text"]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]
            s = SearchEngine(keyword=ips[0], pages=int(ips[1]), type=ips[2])
            for i in s.search(False):
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))

        if task[2] == 1 or task[2] == 2:  # Single and multi
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = []
            res = [list(i) for i in tres]
            for i in res:
               ips.append(i[1])
            for i in ips:
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i, unicode(urllib.urlopen(i), errors="ignore")))

        if task[2] == 3:  # Iterative
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["http://google.com", "num", "0", "10"]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]
            for i in basicnav().iterativenav(i[0], i[1], i[2], i[3]):
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))

        if task[2] == 4:  # Recursive
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["http://google.com", "10", ""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]
            r = recursivenav(i[0], i[1], i[2])
            for i in r.search():
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))


        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)


    def updateStatus(self, tasknum, status):
        self.conn.execute('UPDATE TASKS SET status=? WHERE task=?', (status, tasknum))
        open(self.logfilename, "a").write("TASK[" + str(tasknum) + "]: " + status + "\n")

#
#
# if __name__ == '__main__':
# a = TaskManager([[0, 1, 0, 'Page Navigation', 'Search Engine', [[0, u'Keyword *', u'dsfgdf']]],
# 					 [1, 1, 0, 'Page Navigation', 'Search Engine',
# 					  [[0, u'Keyword *', u'cvbd'], [1, u'Number of Results', u'dfg']]],
# 					 [2, 1, 2, 'Page Navigation', 'URL list',
# 					  [[0, u'URL 1', u'dfg'], [1, u'URL 2', u'dfg'], [2, u'URL 3', u'dfg']]],
# 					 [3, 2, 0, 'Selection', 'HTML attributes', [[0, u'Tag', u'fdg']]]],
# 					logfilename="../logs/tasklog.txt")
# 	a.startAction()
#
