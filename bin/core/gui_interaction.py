import os
from sys import argv, path
import time
from threading import Thread
from BeautifulSoup import BeautifulSoup
import urllib

from PySide.QtGui import *
from PySide.QtCore import *

import gui
import right_item
import left_item
import guidata as data
import constants

import infoDialogs as d

import task44s as tasks
import youtube


class gui_interaction(QDialog, gui.Ui_main_window):
    """
    A Class that handles the interactions between the GUI and the program. The GUI file [gui.py] is to be imported
    and handled here. All Signal Slot interactions are handled by this class.

    1. collecting keywords
    2. collecting all constraints
    3. voice based interactions
    4. display results
    5. options to export data, settings, etc.
    """

    updateSig = Signal()
    vaultSig = Signal()

    def __init__(self):
        super(gui_interaction, self).__init__()

        self.tasks_display_list = []
        self.tasksAdded = []
        self.running = False
        self.taskman = tasks.TaskManager()
        self.items, self.index, self.tabnum = [], 0, 0
        self.currentMainTab = [0, 'main']
        self.starttime = "nill"
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.closebtn.clicked.connect(self.clear)
        self.pause = False
        self.auth = False
        self.th1 = Thread(target=self.looper)
        self.th1.start()
        self.th2 = Thread(target=self.vaultlooper)
        self.th2.start()

        self.initUi()

    def clear(self):
        reload(tasks)
        self.tasks_display_list = []
        self.tasksAdded = []

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUi(self):
        self.center()
        self.startbtn.clicked.connect(self.start)

        self.statusbtn.clicked.connect(lambda: self.ChangeTab("log"))
        self.mvbtn.clicked.connect(lambda: self.ChangeTab("myvault"))
        self.settingsbtn.clicked.connect(lambda: self.ChangeTab("settings"))
        self.helpbtn.clicked.connect(lambda: self.ChangeTab("help"))

        self.updateSig.connect(self.updateUi)
        self.vaultSig.connect(self.vaultchecker)

        self.stackedWidget.setCurrentIndex(1)
        self.currentbtn.setText(data.tabHeadings[1])
        self.prevbtn.setText(data.tabHeadings[0])
        self.nextbtn.setText(data.tabHeadings[2])


        # Help page
        self.textBrowser.setHtml(open("gui/help.html").read())
        self.textBrowser_2.setText(open("gui/abt.html").read())

        # Myvault page
        self.loginbtn.clicked.connect(lambda: self.myvaultlogin(0))
        self.logoutbtn.clicked.connect(lambda: self.myvaultlogin(1))
        self.myvaultclearbtn.clicked.connect(self.myvaultclear)

        # log page
        self.savebtn.clicked.connect(self.savelog)
        self.clearbtn.clicked.connect(self.clearlog)
        self.co_opensave.clicked.connect(lambda: self.stat_commands("open"))
        self.co_openlog.clicked.connect(lambda: self.stat_commands("log"))
        self.closebtn.clicked.connect(lambda: self.stat_commands("stopexec"))

        self.stat_pauseresumebtn.clicked.connect(self.taskman.pauseresume)

        # settings page
        self.ch_fl.clicked.connect(lambda: self.settings("fl"))
        self.ch_tl.clicked.connect(lambda: self.settings("tl"))
        self.ch_ll.clicked.connect(lambda: self.settings("ll"))
        self.ch_ml.clicked.connect(lambda: self.settings("ml"))
        self.ch_tn.clicked.connect(lambda: self.settings("tn"))
        self.ch_re.clicked.connect(lambda: self.settings("re"))
        self.sp_seo.clicked.connect(lambda: self.settings("sp_seo"))
        self.sp_rec.clicked.connect(lambda: self.settings("sp_rec"))



        tabWidgets = [self.filenavlist, self.navnavlist, self.selnavlist, self.constraintlist, self.exportnavlist]
        for tab in data.tabHeadings:
            tabWidgets[self.tabnum].setSpacing(3)
            for i in [i for i in data.btns[self.tabnum]]:
                li = right_item.Item()
                li.label.setText(i)
                li.type.setText(tab)
                listItem = QListWidgetItem(tabWidgets[self.tabnum])
                listItem.setSizeHint(li.sizeHint())
                li.addbtn.clicked.connect(lambda n=self.index: self.newTask(n))
                tabWidgets[self.tabnum].addItem(listItem)
                tabWidgets[self.tabnum].setItemWidget(listItem, li)
                self.items.append(li)
                self.index += 1
            self.tabnum += 1
        self.prevbtn.clicked.connect(self.prev)
        self.nextbtn.clicked.connect(self.next)


    def start(self):
        if self.mainTabs.currentIndex() == 0:
            if len(self.tasks_display_list) == 0:
                self.msg = QMessageBox()
                self.msg.setText("Unable to start, No Tasks added yet!!!")
                self.msg.setWindowTitle("Error!!!")
                self.msg.show()
            else:
                self.starttime = time.time()
                self.taskth = Thread(target=self.taskman.start, args=(self.tasksAdded,))
                self.taskth.setDaemon(True)
                self.taskth.start()
                # self.taskman.start(self.tasksAdded)
                self.clearlog()
                self.ChangeTab("log")
        else:
            self.ChangeTab("main")
            # self.starttime = time.time()


    def newTask(self, i):
        self.mp = d.getInfo([self.items[i].type.text(), self.items[i].label.text()])
        if self.mp.num_ip == 0:
            self.addToTaskList(self.mp.retval())
        elif not self.mp.exec_():
            self.addToTaskList(self.mp.retval())

    def addToTaskList(self, i):
        if i:
            temp = []
            if i[0][2] != "NULLTXT":
                text = "Description:\n"
                for j in i:
                    text += (j[2] + " : " + j[3] + "\n")
                    temp.append([data.inputs[j[0]][j[1]].index(j[2]), j[2], j[3]])
                self.tasks_display_list.append(
                    [len(self.tasks_display_list), data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]], text])
                self.tasksAdded.append(
                    [len(self.tasksAdded), i[0][0], i[0][1], data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]],
                     temp])
            else:
                self.tasks_display_list.append(
                    [len(self.tasks_display_list), data.tabHeadings[i[0][0]], data.btns[i[0][0]][i[0][1]],
                     "No Description"])

    def next(self):
        currentTabIndex = data.tabHeadings.index(self.currentbtn.text())
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 5)
        self.currentbtn.setText(data.tabHeadings[(currentTabIndex + 1) % 5])
        self.prevbtn.setText(data.tabHeadings[currentTabIndex])
        self.nextbtn.setText(data.tabHeadings[(currentTabIndex + 2) % 5])

    def prev(self):
        currentTabIndex = data.tabHeadings.index(self.currentbtn.text())
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 5)
        self.currentbtn.setText(data.tabHeadings[(currentTabIndex - 1) % 5])
        self.prevbtn.setText(data.tabHeadings[currentTabIndex])
        self.nextbtn.setText(data.tabHeadings[(currentTabIndex - 2) % 5])

    def updateUi(self):
        if self.currentMainTab[1] == 'main':
            self.tasklist.clear()
            for task in self.tasks_display_list:
                li = left_item.Item()
                li.label.setText(task[2])
                li.type.setText(task[1])
                if len(task[3])>50:
                    li.desc.setText(task[3][0:50] + "...")
                else:
                    li.desc.setText(task[3])

                li.itemCloseBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.removeItem(x))
                li.itemUpBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.moveItem(x, "Up"))
                li.itemDwnBtn.clicked.connect(lambda x=self.tasks_display_list.index(task): self.moveItem(x, "Down"))

                listItem = QListWidgetItem(self.tasklist)
                listItem.setSizeHint(li.sizeHint())
                self.tasklist.addItem(listItem)
                self.tasklist.setItemWidget(listItem, li)

        elif self.currentMainTab[1]  == 'myvault':
            txt = open(constants.mvlog).read()
            html = ""
            for i in txt.split("\n"):
                tt = i.split(":")
                dt = ":".join(tt[0:3])
                msg = ":".join(tt[3:])
                html += '<span style="color:#ff0000;" >' + dt + '</span> : '
                html += '<span >' + msg + '</span><br/>'
            self.myvaultconsole.setHtml(html)


        elif self.currentMainTab[1] == 'log':
            txt = open(constants.tasklog).read()
            html = ""
            ctsk = "0"
            for i in txt.split("\n"):
                if ":" in i:
                    tt = i.split(":")
                    dt = ":".join(tt[0:3])
                    msg = ":".join(tt[4:])
                    tsk = tt[3]

                    html += '<span style="color:#ff0000;margin-left:0px;" >' + " ".join(dt.split(" ")[3]) + '</span> : '
                    html += '<span style="color:#00ff00;padding-left:10px;" >' + tsk + '</span> : '
                    html += '<span >' + msg + '</span><br/>'

                    if self.starttime != "nill":
                        ctsk = tsk.replace("Task[", "").replace("]", "").replace(" ", "")

                elif "*" in i:
                    html += "<hr/>"
                elif "NEW TASKS" in i:
                    html += '<h5><center><span style="color:#c0c0c0;" ><b>NEW TASKS ADDED</b></span></center></h5>'
            self.console.setHtml(html)
            vscroll = self.console.verticalScrollBar()
            vscroll.setValue(vscroll.maximum())
            if self.starttime != "nill" and self.running:
                dif = time.time() - self.starttime
                hr = dif/(60*60)
                dif %= (60*60)
                min = dif/60
                dif %= 60
                self.stat_ti.setText(str(hr).split(".")[0] + " : " + str(min).split(".")[0] + " : " + str(dif).split(".")[0])
                self.stat_tk.setText(str(len(self.tasks_display_list)))
                self.stat_ct.setText(ctsk)

                progress = map(int, open(constants.prog).read().split(","))
                self.prog_tot.setValue(progress[0])
                self.prog_cur.setValue(progress[1])
            self.running = True if open(constants.prog).read().split(",")[0] != '100' else False

        elif self.currentMainTab[1] == 'settings':
            pass

    def myvaultclear(self):
        open(constants.mvlog, "w").write("")

    def vaultchecker(self):
        if not self.auth:
            pass
        else:
            url = constants.vaultserver + \
                  self.username.text().split("@")[0] + "&p=" + self.password.text()
            txt = urllib.urlopen(url).read()
            li = BeautifulSoup(txt).text.replace("Hosting24 Analytics CodeEnd Of Analytics Code", "").split("\n")
            if len(li[0]) > 0:
                open(constants.mvlog, "a").write("\n" + time.asctime() + ": Found " + str(len(li)) + " link(s)")
                for i in li:
                    open(constants.mvlog, "a").write("\n" + time.asctime() + ": Starting download of " + i)
                    if "youtube.com" in i:
                        if 'watch?' in i:
                            self.v = youtube.youtube()
                            self.v.downloadVideo(str(i))
                        else:
                            youtube.youtube().downloadPlaylist(str(i))

                    else:
                        if not os.path.isdir("../../files"):
                            os.mkdir("../../files")
                        urllib.urlretrieve(i, "../../files/" + i.split("/")[-1])
                    open(constants.mvlog, "a").write("\n" + time.asctime() + ": Finished download of " + i)


    def myvaultlogin(self, logout):
        if logout:
            self.auth = False
            self.username.setDisabled(False)
            self.password.setDisabled(False)
            self.loginbtn.setDisabled(False)
            self.loggedstatus.setText("Not Logged in")
        else:
            if len(self.username.text()) > 0:
                    if len(self.password.text()) > 0:
                        url = "http://projectmagpy.tk/myvault/appvault.php?auth=true&u=" + \
                              self.username.text().split("@")[0] + "&p=" + self.password.text()
                        if "AUTH_TRUE"  in urllib.urlopen(url).read():
                            self.auth = True
                            self.username.setDisabled(True)
                            self.password.setDisabled(True)
                            self.loginbtn.setDisabled(True)
                            self.loggedstatus.setText("Successfully logged in")
                        else:
                            QMessageBox.information(self, "Error", "Login Error, please try again!!!")
                            self.loggedstatus.setText("Login error")

    def removeItem(self, itemNum):
        self.tasks_display_list.pop(itemNum)
        self.tasklist.pop(itemNum)


    def moveItem(self, itemNum, dir):
        if dir == "Up":
            self.tasks_display_list[itemNum], self.tasks_display_list[itemNum - 1] = \
                self.tasks_display_list[itemNum - 1], self.tasks_display_list[itemNum]
        if dir == "Down":
            self.tasks_display_list[itemNum], self.tasks_display_list[itemNum + 1] = \
                self.tasks_display_list[itemNum + 1], self.tasks_display_list[itemNum]

    def ChangeTab(self, name, sec=0):
        if sec == 0:
            self.mtabs = ['main', 'log', 'myvault', 'settings', 'help']
            self.newTabName = name
            self.anim()

        else:
            if self.mainTabs.currentIndex() == 0 and self.newTabName != "main":
                self.startbtn.setText("Home")
                self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
            elif self.mainTabs.currentIndex() == 0 and self.newTabName == "main":
                self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
            elif self.newTabName == "main":
                self.startbtn.setText("Start")
                self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))
            else:
                self.mainTabs.setCurrentIndex(self.mtabs.index(self.newTabName))

            self.restore()

        self.currentMainTab = [self.mtabs.index(self.newTabName), self.newTabName]


    def anim(self):
        self.geo = self.mainTabs.geometry()
        self.hideAnimation = QPropertyAnimation(self.mainTabs, "geometry")
        self.hideAnimation.setDuration(150)
        self.mainTabs.startGeometry = QRect(self.mainTabs.geometry())
        self.mainTabs.endGeometry = QRect(self.mainTabs.geometry().getRect()[0], self.mainTabs.geometry().getRect()[1],
                                          self.mainTabs.geometry().width(), 0)
        self.hideAnimation.setStartValue(self.mainTabs.startGeometry)
        self.hideAnimation.setEndValue(self.mainTabs.endGeometry)
        self.hideAnimation.start()
        self.hideAnimation.finished.connect(lambda: self.ChangeTab("", sec=1))


    def restore(self):
        self.hideAnimation1 = QPropertyAnimation(self.mainTabs, "geometry")
        self.hideAnimation1.setDuration(100)
        self.mainTabs.startGeometry = QRect(self.mainTabs.geometry())
        self.mainTabs.endGeometry = QRect(self.geo)
        self.hideAnimation1.setStartValue(self.mainTabs.startGeometry)
        self.hideAnimation1.setEndValue(self.mainTabs.endGeometry)
        self.hideAnimation1.start()


    def savelog(self):
        txt = open(constants.tasklog).read()
        open(constants.savelogloc, 'w').write(txt)
        open(constants.tasklog, 'a').write("\n# Logs Saved to:  " + constants.savelogloc)

    def clearlog(self):
        open(constants.tasklog, 'w').write("\n# Logs Cleared")

    def settings(self, c):
        default = "mvlog = '../logs/mvlog.txt'\n" \
                  "prog = '../logs/prog.txt'\n" \
                  "vaultserver = 'http://projectmagpy.tk/myvault/appvault.php?link=true&u='\n" \
                  "savelogloc = 'C://savedlog.txt'"

        tfileloc = constants.fileloc
        ttextop = constants.texttop
        ttasklog = constants.tasklog
        tmvloc = constants.mvloc
        ttaskdbloc = constants.taskdbloc
        tsearch_algo = constants.search_algo

        if c == "fl":
            tfileloc = self.text_fl.text()
        elif c == "tl":
            ttextop = self.text_tl.text()
        elif c == "ll":
            ttasklog = self.text_ll.text()
        elif c == "ml":
            tmvloc = self.text_ml.text()
        elif c == "tn":
            ttaskdbloc = self.text_tn.text()
        elif c == "re":
            tfileloc = '../files/'
            ttextop = '../data.txt'
            ttasklog = '../logs/tasklog.txt'
            tmvloc = '../files/'
            ttaskdbloc = 'tasksdb.db'
            tsearch_algo = 'seo'
        elif c == "sp_rec":
            tsearch_algo = 'rec'
        elif c == "sp_seo":
            tsearch_algo = 'seo'

        full = default + "\n" + \
               "fileloc = '" + tfileloc + "'\n" + \
               "texttop = '" + ttextop + "'\n" + \
               "tasklog = '" + ttasklog + "'\n" + \
               "mvloc = '" + tmvloc + "'\n" + \
               "taskdbloc = '" + ttaskdbloc + "'\n" + \
               "search_algo = '" + tsearch_algo + "'\n"
        open("constants.py", "w").write(full)
        reload(constants)
        self.close()
        os.system("gui_interaction.py")


    def stat_commands(self, c):
        if c == "open":
            cmd = constants.fileloc.replace("/", "\\")
            open("commands/openfiles.bat", "w").write("@echo off\nexplorer " + cmd)
            os.system("commands\\openfiles.bat")

        elif c == "log":
            cmd = constants.tasklog.replace("/", "\\")
            open("commands/openlog.bat", "w").write("@echo off\nnotepad " + cmd)
            os.system("commands\\openlog.bat")

        elif c == "stopexec":
            self.close()
            os.system("gui_interaction.py restart")

    def looper(self):
        while True:
            time.sleep(1)
            self.updateSig.emit()

    def vaultlooper(self):
        while True:
            time.sleep(3)
            self.vaultSig.emit()


if __name__ == '__main__':
    argv.append("building")
    app = QApplication(argv)
    if "restart" not in argv and "building" not in argv:
        os.system("commands\\minimize.bat")
        ss = QSplashScreen(QPixmap("images/splash.png"))
        ss.show()
        ss.showMessage("Loading Components", alignment=Qt.AlignBottom|Qt.AlignHCenter, color=Qt.white)
        mp = gui_interaction()
        time.sleep(2)
        ss.showMessage("Initialising Components", alignment=Qt.AlignBottom|Qt.AlignHCenter, color=Qt.white)
        time.sleep(3)
        ss.showMessage("Finished Loading. Welcome to MagPy.", alignment=Qt.AlignBottom|Qt.AlignHCenter, color=Qt.white)
        time.sleep(1)
        mp.show()
        ss.hide()
    else:
        mp = gui_interaction()
        mp.show()
    app.exec_()