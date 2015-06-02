from navmanager import *
from filemanager import *
from export import *
import constants
import time
from threading import Thread
import speech
import re as reg

class TaskManager():
    def __init__(self):
        self.stop = False

    def start(self, tasks, resume=False):
        self.speechcontent = ""
        open(constants.tasklog, "a").write("\n**************\nNEW TASKS ADDED\n**************\n")
        self.tasklist = tasks
        self.funcs = [self.file, self.nav, self.sel, self.const, self.exp]

        if not resume:
            self.tasks, self.inputs, self.results = [], [], []
            self.tasknum = 0
            self.initlists()

        self.updateprog(self.tasknum, (self.tasknum*100)/len(self.tasks))
        if self.checkcombis():
            self.updatestat(0, "Check completed, starting tasks")
            self.updatestat(0, "Initiated")
            for n in range(self.tasknum, len(self.tasks)):
                if self.stop:
                    break
                self.tasknum = n
                t = self.tasks[n]
                self.funcs[t[1]](n)
                self.updateprog(n, 1)
                self.updatestat(n, "Completed")
                if (n+1) < len(self.tasks):
                    self.updatestat(n+1, "Initiated")
            self.updateprog(n+1, 100)
            self.updatestat(n, "Tasks Completed")


    def file(self, n):
        self.updatestat(n, "Starting File Download ")
        self.updateprog(n, 0)
        t = self.tasks[n]
        i = self.inputs[n]

        self.formats = [
            'jpg,png,svg',
            'mp4,flv'
            'docx,pdf,doc,ppt,pptx'
        ]

        if t[2] == 0 or t[2] == 1 or t[2] == 2:  # Images, vid ,regex
            ips = ["url"]
            for x in i[3]:
                ips[0] = x[2]
            if ips[0] == "url":
                for res in self.results[n-1][1]:
                    if t[2] == 0:
                        for pr in filemanager(url=res[0], direct=False, format=self.formats[t[2]]).manageimages():
                            self.updateprog(n, pr)
                    else:
                        for pr in filemanager(url=res[0], direct=False, format=self.formats[t[2]]).managefiles():
                            self.updateprog(n, pr)
            else:
                if t[2] == 0:
                    for pr in filemanager(url=ips[0], direct=False, format=self.formats[t[2]]).manageimages():
                        self.updateprog(n, pr)
                else:
                    for pr in filemanager(url=ips[0], direct=False, format=self.formats[t[2]]).managefiles():
                        self.updateprog(n, pr)

        if t[2] == 3:  # Regex
            ips = ["url", "pattern"]
            for x in i[3]:
                ips[x[0]] = x[2]
            if ips[0] == "url":
                for res in self.results[n-1][1]:
                    for pr in filemanager(url=res[0], direct=False, format="").manageregex(ips[1]):
                        self.updateprog(n, pr)
            else:
                for pr in filemanager(url=ips[0], direct=False, format="").manageregex(ips[1]):
                    self.updateprog(n, pr)



    def nav(self, n):
        self.updatestat(n, "Starting Navigation ")
        self.updateprog(n, 0)
        t = self.tasks[n]
        i = self.inputs[n]
        if t[2] == 0:  # SearchEngine
            ips = ["none", "1", "text"]
            for x in i[3]:
                ips[x[0]] = x[2]
            prog, tem = 0, []
            if ips[2] in ["images", "img", "jpg", "pictures"]:
                import imagedn
                for prg in imagedn.download(ips[0]):
                    self.updateprog(n, prg)
                self.results.append([n, []])
            else:
                for res in SearchEngine(ips[0], int(ips[1]), ips[2]).search():
                    prog += 1
                    self.updatestat(n, "Processing: url no. " + str(prog))
                    self.updateprog(n, float(prog*100)/res[2])
                    tem.append([res[0], res[1]])
                self.results.append([n, tem])


        if t[2] == 1:  # Single URL
            url = i[3][0][2]
            self.results.append([n, [[url, urllib.urlopen(url).read()]]])


        if t[2] == 2:  # Multi URL
            temp = []
            prog = 0
            for x in i[3]:
                prog += 1
                temp.append([x[2], urllib.urlopen(x[2]).read()])
                self.updateprog(n, (prog*100)/len(i[3]))
            self.results.append([n, temp])

        if t[2] == 3:  # Iterative
            ips = ["base", "type", "0", "0"]
            for x in i[3]:
                ips[x[0]] = x[2]
            if ips[0] == "base":
                self.updateerrorndstop(n)
            prog, tem, tot = 0, [], 0
            urls = []
            if ips[1] == "num" or ips[2].isdigit():
                start, stop = int(ips[2]), int(ips[3])
                for index in xrange(start, stop+1):
                    urls.append(ips[0].replace("%d", str(index)))
            for url in urls:
                prog += 1
                tem.append([url, urllib.urlopen(url).read()])
                self.updateprog(n, (prog*100)/tot)
            self.results.append(tem)


        if t[2] == 4:  # Recursive
            pass

        self.updateprog(n, 100)
        self.updatestat(n, "Obtained data")

    def sel(self, n):
        self.updatestat(n, "Selecting required data")
        self.updateprog(n, 0)
        t = self.tasks[n]
        i = self.inputs[n]
        if t[2] == 0:
            tag, clas, id = "", "", ""
            for ip in i[3]:
                if "tag" in ip[1].lower():
                    tag = ip[2].lower()
                if "class" in ip[1].lower():
                    clas = ip[2].lower()
                if "id" in ip[1].lower():
                    id = ip[2].lower()
            if tag == "":
                self.updateerrorndstop(n)
            gg = []
            for r in self.results:
                if r[0] == n-1:
                    for rx in r[1]:
                        tempres = []
                        try:
                            b = BeautifulSoup(rx[1])
                            if id == "":
                                if clas == "":
                                    for bb in b.findAll(tag):
                                        tempres.append(bb.text)
                                else:
                                    for bb in b.findAll(tag, attrs={"class": clas}):
                                        tempres.append(bb.text)
                            else:
                                if clas == "":
                                    for bb in b.findAll(tag, attrs={"id": id}):
                                        tempres.append(bb.text)
                                else:
                                    for bb in b.findAll(tag, attrs={"id": id, "class": clas}):
                                        tempres.append(bb.text)
                            gg.append([rx[0], "<p>" + "</p></p>".join(tempres) + "</p>"])
                            print gg
                        except:
                            pass
            self.results.append([n, gg])

        if t[2] == 1:
            for r in self.results:
                tempres = []
                if r[0] == n-1:
                    r[0] = n
                    self.results.append([r])

        if t[2] == 2:
            for r in self.results:
                tempres = []
                if r[0] == n-1:
                    for rex in r[1]:
                        b = BeautifulSoup(rex[1])
                        txt = "<p>" + "</p><p>".join(dd for dd in b.find("body").findAll("p")) + "</p>"
                        tempres.append([rex[0], txt])
                self.results.append([n, tempres])

        if t[2] == 3:
            pat = i[3][0][2]
            for r in self.results:
                tempres = []
                if r[0] == n-1:
                    for rx in r[1]:
                        tempres.append([rx[0], "<p>" + "</p><p>".join(reg.findall(pat, rx[1])) + "</p>"])
            self.results.append([n, tempres])

        self.updatestat(n, "Selection completed")
        self.updateprog(n, 100)


    def const(self, n):
        self.updatestat(n, "Applying Constraints ")
        self.updateprog(n, 0)
        t = self.tasks[n]
        i = self.inputs[n]
        prevres = []

        for r in self.results:
                if r[0] == n-1:
                    prevres = r[1]

        if t[2] == 0:  # "size",  "consists of", "not consists of"
            ips = [""]
            for x in i[3]:
                ips[x[0]] = x[2]
            prog, tem = 0, []
            for dt in prevres:
                ht = "\n".join([ps for ps in BeautifulSoup(dt[1]).find("body").findAll("p")])
                wds = 0
                lim = int(ips[0])
                final = ""
                for gh in ht.split("\n"):
                    for ij in gh.split(" "):
                        wds += 1
                        final += ij
                        if wds>lim and not "." in ij:
                            continue
                        elif wds>lim:
                            break
                    if wds>lim:
                        break
                    else:
                        final += "\n"
                tem.append([0, final])
            self.results.append([n, tem])

        if t[2] == 1 or t[2] == 2:
            ips = [""]
            for x in i[3]:
                ips[x[0]] = x[2]
            prog, tem = 0, []
            for dt in prevres:
                if t[2] == 1:
                    if ips[0] in dt[1] and dt[1].count(ips[0])>5:
                        tem.append([0, final])
                else:
                    if ips[0] in dt[1] and dt[1].count(ips[0])>5:
                        tem.append([0, final])
            self.results.append([n, tem])

        self.updatestat(n, "Finished filtering data")
        self.updateprog(n, 100)


    def exp(self, n):
        self.updatestat(n, "Exporting obtained data")
        self.updateprog(n, 0)
        t = self.tasks[n]
        i = self.inputs[n]
        r = self.results[n-1][1]
        self.results.append(self.results[n-1])
        self.results[n][0] = n
        print len(r)
        if t[2] == 0:  # docx
            fname = i[3][0][2]
            data = []
            for item in r:
                try:
                    b = BeautifulSoup(item[1])
                    l = len(r)
                    hascontent = 0
                    # for tt in b.findAll("p"):
                    #     if len(tt.text) > 10:
                    #         hascontent += 1
                    # if hascontent>2:
                    self.updateprog(n, (r.index(item)*100)/l)
                    txt = "\n".join([temp.text for temp in b.findAll("p")])
                    if len(txt.replace("\n", ""))> 10:
                        if not b.find("title"):
                            title = fname
                        else:
                            title = b.find("title").text
                        data.append([title, txt])
                        self.updatestat(n, "Exporting: " + title)
                except:
                    print "Error " + item
            print data
            d = docx(data, fname)

        if t[2] == 1:  # text
            fname = i[3][0][2]
            for item in r:
                try:
                    b = BeautifulSoup(item[1])
                    txt = "\n".join([temp.text for temp in b.findAll("p")])
                    if len(txt.replace("\n", ""))> 20:
                        open(constants.fileloc + fname + ".txt", "a").write(txt)
                except:
                    pass

        if t[2] == 2:
            for item in r:
                b = BeautifulSoup(item[1])
                txt = "\n".join([temp.text for temp in b.findAll("p")])
                self.speechcontent += txt + ".\n\n"
            Thread(target=self.voice, args=(self.speechcontent,)).start()

        self.updatestat(n, "Export completed")
        self.updateprog(n, 100)


    def voice(self, x):
        speech.say(x)

    def initlists(self):
        for l in self.tasklist:
            t, i = [], []
            for x in l[:3]:
                t.append(x)
                i.append(x)
            i.append(l[5])
            self.tasks.append(t)
            self.inputs.append(i)

            # [0, 1, 0, [[0, u'Keyword *', u'dsfgdf']]]
            # [1, 1, 0, [[0, u'Keyword *', u'cvbd'], [1, u'Number of Results', u'3']]]
            # [2, 1, 2, [[0, u'URL 1', u'dfg'], [1, u'URL 2', u'dfg'], [2, u'URL 3', u'dfg']]]
            # [3, 2, 0, [[0, u'Tag', u'fdg']]]


    def checkcombis(self):
        if self.tasks[0][0] not in [0, 1]:
            self.updateerrorndstop(0)
            return False
        return True

    #
    # for i in xrange(0, len(self.tasks)-1):
    #         p1, p2 = self.tasks[i][1], self.tasks[i+1][1]
    #         if p1 == 0:
    #             if p2 ==



    def updatestat(self, tsk, msg):
        open(constants.tasklog, "a").write("\n" + time.asctime() + ": Task[" + str(tsk) + "] : " + msg)

    def updateprog(self, tsk, prog, er=0):
        tot = str((tsk*100)/len(self.tasks)).split(".")[0]
        cur = str(prog).split(".")[0]
        open("../logs/prog.txt", "w").write(tot + "," + cur + "," + str(er))
        # print tot+cur

    def updateerrorndstop(self, task):
        open(constants.tasklog, "a").write("\n" + time.asctime() + ": ERROR : Invalid task input.")
        self.updateprog(task, 0, 1)
        self.stop = True


    def pauseresume(self):
        import pausendresume as pr
        if os.path.isfile("save.p"):
            [self.tasknum, self.tasks, self.inputs, self.results] = pr.resume()
            self.start([], resume=True)
        else:
            pr.pause(self.tasknum, self.tasks, self.inputs, self.results)
            self.stop = True



if __name__ == '__main__':
    a = TaskManager().start([[0, 1, 0, 'Page Navigation', 'Search Engine', [[0, u'Keyword *', u'dsfgdf']]],
                     [1, 1, 0, 'Page Navigation', 'Search Engine',
                      [[0, u'Keyword *', u'cvbd'], [1, u'Number of Results', u'3']]],
                     [2, 1, 2, 'Page Navigation', 'URL list',
                      [[0, u'URL 1', u'dfg'], [1, u'URL 2', u'dfg'], [2, u'URL 3', u'dfg']]],
                     [3, 2, 0, 'Selection', 'HTML attributes', [[0, u'Tag', u'fdg']]]])
