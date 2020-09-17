# -*- coding: utf-8 -*-

# usr/bin/python3

# logic starts at 197 and ends at 324

import os, webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 931)
        MainWindow.setFixedWidth(1118)
        MainWindow.setFixedHeight(931)

        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")

        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:#353638;\n"
"\n"
"")
        self.file_opts={
        "fileOpened":False,
        "absfileName":None,
        "indirfileName":None
        }

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(350, 0, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qedit_label = QtWidgets.QLabel(self.horizontalLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(18)

        self.qedit_label.setFont(font)
        self.qedit_label.setStyleSheet("QLabel::!hover{color:#1fade0;}\n"
"QLabel::hover{color: cyan;}")


        self.qedit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qedit_label.setObjectName("qedit_label")
        self.horizontalLayout.addWidget(self.qedit_label)
        self.textspace = QtWidgets.QTextEdit(self.centralwidget)
        self.textspace.setStyleSheet("color:white;")
        self.textspace.setGeometry(QtCore.QRect(0, 60, 1121, 821))
        self.textspace.setAcceptRichText(True)

        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)

        self.textspace.setFont(font)
        self.textspace.setTextColor(QtGui.QColor(255, 255, 255))
        self.textspace.setObjectName("textspace")
        self.qedit_version = QtWidgets.QLabel(self.centralwidget)
        self.qedit_version.setGeometry(QtCore.QRect(950, 0, 160, 49))

        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(14)

        self.qedit_version.setFont(font)
        self.qedit_version.setStyleSheet("color:orange;")
        self.qedit_version.setObjectName("qedit_version")
        self.editingFile = QtWidgets.QLabel(self.centralwidget)
        self.editingFile.setGeometry(QtCore.QRect(0, 8, 217, 41))

        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(14)

        self.editingFile.setFont(font)
        self.editingFile.setStyleSheet("color:lightgreen;")
        self.editingFile.setText("")
        self.editingFile.setObjectName("editingFile")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 23))


        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)


        self.menubar.setFont(font)
        self.menubar.setStyleSheet("color:white;")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)


        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)


        self.menuFile.setFont(font)
        self.menuFile.setStyleSheet("QMenu:selected{color:#346fed; }")
        self.menuFile.setObjectName("menuFile")
        self.menuFont = QtWidgets.QMenu(self.menubar)


        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)


        self.menuFont.setFont(font)
        self.menuFont.setStyleSheet("QMenu:selected{color:#346fed; }")
        self.menuFont.setObjectName("menuFont")
        self.menuHelp = QtWidgets.QMenu(self.menubar)

        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)

        self.menuHelp.setFont(font)
        self.menuHelp.setStyleSheet("QMenu:selected{color:#346fed; }")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionChange_Font = QtWidgets.QAction(MainWindow)
        self.actionChange_Font.setObjectName("actionChange_Font")
        self.actionGoto_Website = QtWidgets.QAction(MainWindow)
        self.actionGoto_Website.setObjectName("actionGoto_Website")
        self.actionFont_color = QtWidgets.QAction(MainWindow)
        self.actionFont_color.setObjectName("actionFont_color")


        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFont.addAction(self.actionChange_Font)
        self.menuFont.addAction(self.actionFont_color)
        self.menuHelp.addAction(self.actionGoto_Website)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFont.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())


        self.actionSave_As.triggered.connect(self.saveAsAction)
        self.actionSave.triggered.connect(self.saveAction)
        self.actionChange_Font.triggered.connect(self.changeFont)
        self.actionClear.triggered.connect(self.clearWindow)
        self.actionOpen.triggered.connect(self.fbrowserOpen)
        self.actionFont_color.triggered.connect(self.changeFontColor)
        self.actionGoto_Website.triggered.connect(self.openWebsite)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Qedit"))
        self.qedit_label.setText(_translate("MainWindow", "Qedit"))
        self.qedit_version.setText(_translate("MainWindow", "Version- 0.0.1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFont.setTitle(_translate("MainWindow", "Font"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionChange_Font.setText(_translate("MainWindow", "Change Font"))
        self.actionGoto_Website.setText(_translate("MainWindow", "Goto Website"))
        self.actionFont_color.setText(_translate("MainWindow", "Font color"))

    def openWebsite(self):
        webbrowser.open("https://github.com/Icelain/Qedit")

    def changeFontColor(self):
        color = QtWidgets.QColorDialog.getColor()
        self.textspace.setTextColor(color)

    def changeFont(self):
          font, valid=QtWidgets.QFontDialog.getFont()
          if valid:
              self.textspace.setFont(font)

    def fbrowserOpen(self):
        try:
            dname=QtWidgets.QFileDialog()
            dname.setFileMode(QtWidgets.QFileDialog.ExistingFile)
            fname=dname.getOpenFileName(None, "Open File", os.getcwd(),"All files(*.*)")
            mainFile=fname[0]

            indirFname=os.path.basename(mainFile)

            mainFileText=""
            fileList=[]
            with open(mainFile,"r") as fileObj:
                for line in fileObj.readlines():
                    fileList.append(line)

            fileList.reverse()
            for line in fileList:
                mainFileText=line+mainFileText
            self.textspace.setPlainText(mainFileText)
            self.editingFile.setText(indirFname)

            self.file_opts["fileOpened"]=True
            self.file_opts["indirfileName"]=indirFname
            self.file_opts["absfileName"]=mainFile
        except:
            pass

    def clearWindow(self):
        self.textspace.setText("")

    def saveAction(self):
        textData=self.textspace.toPlainText()

        if not self.file_opts["fileOpened"]:
            try:
                dname=QtWidgets.QFileDialog()
                dname.setFileMode(QtWidgets.QFileDialog.AnyFile)
                fname=dname.getSaveFileName(None,"Save File",os.getcwd(),"All files(*.*)")

                indirFname=os.path.basename(fname[0])
                MainFile=fname[0]

                with open(MainFile, "w+") as sv2FileObj:
                    sv2FileObj.seek(0)
                    sv2FileObj.truncate()
                    sv2FileObj.write(textData)

                fileList=[]
                mainFileText=""
                with open(MainFile,"r") as fileObj:
                    for line in fileObj.readlines():
                        fileList.append(line)

                fileList.reverse()
                for line in fileList:
                    mainFileText=line+mainFileText
                self.textspace.setPlainText(mainFileText)
                self.editingFile.setText(indirFname)

                self.file_opts["fileOpened"]=True
                self.file_opts["indirfileName"]=indirFname
                self.file_opts["absfileName"]=MainFile
            except:
                pass

        else:
            with open(self.file_opts["absfileName"],"w+") as svFileObj:
                svFileObj.seek(0)
                svFileObj.truncate()
                svFileObj.write(textData)

    def saveAsAction(self):
        textData=self.textspace.toPlainText()
        if not self.file_opts["fileOpened"]:
            try:
                dname=QtWidgets.QFileDialog()
                dname.setFileMode(QtWidgets.QFileDialog.AnyFile)
                fname=dname.getSaveFileName(None,"Save File",os.getcwd(),"All files(*.*)")

                indirFname=os.path.basename(fname[0])
                MainFile=fname[0]

                with open(MainFile, "w+") as sv2FileObj:
                    sv2FileObj.seek(0)
                    sv2FileObj.truncate()
                    sv2FileObj.write(textData)

                fileList=[]
                mainFileText=""
                with open(MainFile,"r") as fileObj:
                    for line in fileObj.readlines():
                        fileList.append(line)

                fileList.reverse()
                for line in fileList:
                    mainFileText=line+mainFileText
                self.textspace.setPlainText(mainFileText)
                self.editingFile.setText(indirFname)

                self.file_opts["fileOpened"]=True
                self.file_opts["indirfileName"]=indirFname
                self.file_opts["absfileName"]=MainFile
            except:
                pass

        else:
            try:
                dname=QtWidgets.QFileDialog()
                dname.setFileMode(QtWidgets.QFileDialog.AnyFile)
                fname=dname.getSaveFileName(None,"Save File",os.getcwd(),"All files(*.*)")
                with open(fname[0], "w+") as sv2FileObj:
                    sv2FileObj.seek(0)
                    sv2FileObj.truncate()
                    sv2FileObj.write(textData)
            except:
                pass




if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

