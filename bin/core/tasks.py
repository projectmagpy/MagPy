import sqlite3
from navmanager import *
from filemanager import *
from export import *
import constants
import speech, time


class TaskManager():
    def start(self, tasks, logfilename=constants.tasklog):
        self.speechcontent = ""
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
            res = [list(tres.fetchone())[1]]
            for i in res:
               ips[0] = i

            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            r1 = "<p>"
            for m in html.fetchall():
                b = BeautifulSoup(list(m)[0])
                if ips[2] != "":
                    r1 += b.find(ips[0], attrs={"id": ips[2]})
                else:
                    r1 += " :: ".join([i.text for i in b.findAll(str(ips[0]))])
            r1 += "</p>"
            try:
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, " ", "<p>" + unicode(r1, errors="ignore") + "</p>"))
            except:
                self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, " ", r1.encode("utf-8")))



        if task[2] == 3:  # From Text
            pass
        if task[2] == 4:  # Regular Expressions
            pass

        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)



    def constrain(self, tnum):
        task = self.tasklist[tnum]
        if task[2] == 0:  # Size
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                if "<p>" in ht2:
                    ht = "\n".join([i.text for i in b.findAll("p")])
                else:
                    ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                try:
                    title = b.find("title").text
                except:
                    title="Exported from magpy"
                hh=0
                while True:
                    if ht[int(ips[0]) + hh] == ".":
                        ht = ht[0:(int(ips[0]) + hh)]
                        break
                    hh += 1
                k += 1

        if task[2] == 1:  # Count
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                if "<p>" in ht2:
                    ht = "\n".join([i.text for i in b.findAll("p")])
                else:
                    ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                try:
                    title = b.find("title").text
                except:
                    title="Exported from magpy"
                hh=0
                while True:
                    if ht[int(ips[0]) + hh] == ".":
                        ht = ht[0:(int(ips[0]) + hh)]
                        break
                    hh += 1
                k += 1

        if task[2] == 2 or task[2] == 3:  # Contains nd not
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                if "<p>" in ht2:
                    ht = "\n".join([i.text for i in b.findAll("p")])
                else:
                    ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                if task[2] == 2:
                    if ips[0] not in ht:
                        self.conn.execute("UPDATE RESULTS set task=\"-1\" WHERE html=?", (ht2,))
                if task[2] == 3:
                    if ips[0] in ht:
                        self.conn.execute("UPDATE RESULTS set task=\"-1\" WHERE html=?", (ht2,))





        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)



    def export(self, tnum):
        task = self.tasklist[tnum]
        if task[2] == 0:  # Docx
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                # if "<p>" in ht2:
                ht = "\n".join([i.text for i in b.findAll("p")])
                # else:
                #     ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                try:
                    title = b.find("title").text
                except:
                    title="Exported from magpy"
                docx(title, ht).export(str(k) + ips[0])
                self.speechcontent += title + ".\n" + ht
                k += 1
            speech.say(self.speechcontent)

        if task[2] == 1:  # to Text
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                if "<p>" in ht2:
                    ht = "\n".join([i.text for i in b.findAll("p")])
                else:
                    ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                text(ht).export(ips[0])

        if task[2] == 2:  # to voice
            html = self.conn.execute("SELECT html from RESULTS WHERE task=?", (tnum-1,))
            # print list(html.fetchone())[0]
            k = 0
            for h in html.fetchall():
                ht2 = list(h)[0]
                b = BeautifulSoup(ht2)

                if "<p>" in ht2:
                    ht = "\n".join([i.text for i in b.findAll("p")])
                else:
                    ht = b.text

                tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
                ips = [""]
                res = [list(i) for i in tres]
                for i in res:
                   ips[0] = i[1]
                try:
                    title = b.find("title").text
                except:
                    title="Exported from magpy"
                self.speechcontent += title + ".\n" + ht
                k += 1


        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)


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
                b = BeautifulSoup(list(html.fetchone())[0])
                data = "\n".join(i.text for i in b.findAll("p"))
            else:
                html = requests.get(ips[0])
                b = BeautifulSoup(list(html.fetchone())[0])
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
                b = BeautifulSoup(list(html.fetchone())[0])
            else:
                html = requests.get(ips[0])
                b = BeautifulSoup(html.text)

            for im in b.findAll("img"):
                if ".jpg" in im['src']:
                    if "http" in im["src"]:
                        urllib.urlretrieve(im["src"], constants.fileloc + "/" + im["src"].split("/")[-1])
                    else:
                        urllib.urlretrieve(ips[0] + im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])

        if task[2] == 2:  # videos
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
                b = BeautifulSoup(list(html.fetchone())[0])
            else:
                html = requests.get(ips[0])
                b = BeautifulSoup(html.text)

            for im in b.findAll("a"):
                try:
                    if "mp4" in im["href"]:
                        if "http" in im["href"]:
                            urllib.urlretrieve(im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])
                        else:
                            urllib.urlretrieve(ips[0] + im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])
                except:
                    pass

        if task[2] == 3:  # files
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = [""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]

            data = ""
            if len(ips) == 0:
                link, html = self.conn.execute("SELECT link, html from RESULTS WHERE task=?", (tnum-1,))
                b = BeautifulSoup(list(html.fetchone())[0])
            else:
                html = requests.get(ips[0])
                b = BeautifulSoup(html.text)
            for im in b.findAll("a"):
                try:
                    if "pdf" in im["href"]:
                        if "http" in im["href"]:
                            urllib.urlretrieve(im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])
                        else:
                            urllib.urlretrieve(ips[0] + im["href"], constants.fileloc + "/" + im["href"].split("/")[-1])
                except:
                    pass

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
                html = urllib.urlopen(ips[0]).read()
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
                try:
                    self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))
                except:
                    pass

        if task[2] == 1 or task[2] == 2:  # Single and multi
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = []
            res = [list(i) for i in tres]
            for i in res:
               ips.append(i[1])
            for i in ips:
                try:
                    self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i, unicode(urllib.urlopen(i).read(), errors="ignore")))
                except:
                    pass

        if task[2] == 3:  # Iterative
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["http://google.com", "num", "0", "10"]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]
            for i in basicnav().iterativenav(i[0], i[1], i[2], i[3]):
                try:
                    self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))
                except:
                    pass

        if task[2] == 4:  # Recursive
            tres = self.conn.execute("SELECT ipnum, value from INPUTS WHERE task=?", (tnum,))
            ips = ["http://google.com", "10", ""]
            res = [list(i) for i in tres]
            for i in res:
               ips[i[0]] = i[1]
            r = recursivenav(i[0], i[1], i[2])
            for i in r.search():
                try:
                    self.conn.execute("INSERT INTO RESULTS VALUES (?, ?, ?)", (tnum, i[0], unicode(i[1], errors="ignore")))
                except:
                    pass


        self.updateStatus(self.tasklist[tnum][0], "Task Completed")
        self.updateStatus(self.tasklist[tnum+1][0], "Task Initiated")
        self.funcs[self.tasklist[tnum+1][1]](tnum+1)


    def updateStatus(self, tasknum, status):
        self.conn.execute('UPDATE TASKS SET status=? WHERE task=?', (status, tasknum))
        open(self.logfilename, "a").write("\n" + time.asctime() + ": TASK[" + str(tasknum) + "]: " + status + "\n")

    def talk(self):
        for i in self.speechcontent.split("."):
            speech.say(i)

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
