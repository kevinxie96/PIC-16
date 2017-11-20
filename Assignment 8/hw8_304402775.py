# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:17:33 2017

@author: kevin_000
"""

# Challenge 1
#%%
"""
create a class called maxlist. This class creates objects
that have a value attribute, which is a python list of integers. The class has a function delmax, which
deletes a maximal value from the list (making the list shorter), and a function addmax, which adds an
element to the list which is 1 greater than the current max value
"""

class maxlist(object):
    def __init__(self,val=[]):
        self.val=val
        
    def delmax(self):
        self.val.remove(self.findmax())
        return self.val
            
    def addmax(self):
        self.val.append(self.findmax()+1)
        return self.val
        
    def findmax(self):
        maximum = self.val[0]
        for i in self.val[1:]:
            if i >maximum:
                maximum = i
        return maximum

listMax = [1,2,3]
d = maxlist(listMax)
print (d.addmax())
print (d.delmax())

# Challenge 2
#%%
"""
Use TkInter to create an n × n knight’s tour puzzle game.
"""
import random
import tkinter as Tk #or tkinter in v.3
root = Tk.Tk()

class knights_tour(object):
    def __init__(self,n):
        self.n=n
        self.sqr = 0
        self.lastMoveId = 0
        self.width = 480
        self.height = 480
        factor = int(480/self.n)
        factor2 = int(2*480/self.n)
        self.validKnightMoves = [(factor,factor2),(-factor,factor2),(factor,-factor2),(-factor,-factor2),(-factor2,-factor),(-factor2,factor),(factor2,-factor),(factor2,factor)]
        self.canvas = Tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.pack()
        self.createGame()
    def createBoard(self):
        for r in range(self.n-1, -1, -1):
            for c in range(self.n):
                if c&1 ^ r&1:
                    fill = 'white'
                else:
                    fill = 'black'
                coords = (c*self.width/self.n+4, r*self.width/self.n+4, c*self.width/self.n+self.width/self.n, r*self.width/self.n+self.width/self.n)
                self.canvas.create_rectangle(coords,
                                        fill=fill,
                                        width=2,
                                        state='disabled')
    def createGame(self):
        self.createBoard()
        self.createAndPlaceKnight()
        self.canvas.bind("<Button-1>",self.rectangle)
        root.mainloop()
    def rectangle(self,event):
        closestSquare = self.canvas.find_closest(event.x,event.y)
        if self.canvas.itemcget(closestSquare,'fill') == "#ADD8E6":   # can't return to square already visited
            return
        coords = self.canvas.coords(closestSquare)
        if self.validSquare((coords[0], coords[1])):   # check if it's a valid square visitable by knight
            self.sqr = closestSquare[0]
            self.canvas.create_rectangle(coords, fill="#ADD8E6")
            self.canvas.delete(self.lastMoveId)
            self.lastMoveId = 0
            itemId = self.canvas.create_text((coords[0], coords[1]), font=('Courier 30'), text='\u2658',
                               anchor='nw', tags='knight')
            self.lastMoveId = itemId
    def createAndPlaceKnight(self):
        sqr = int( 1 + random.random() * 64)
        self.sqr = sqr
        coords = self.canvas.coords((sqr, ))
        self.canvas.create_rectangle(coords, fill="#ADD8E6")
        itemId = self.canvas.create_text(coords[0], coords[1], font=('Courier 30'), text='\u2658',
                           anchor='nw', tags='knight')
        self.lastMoveId = itemId
        
    def validSquare(self,coords):
        coordsX = coords[0]
        coordsY = coords[1]
        currentCoords = self.canvas.coords((self.sqr, ))
        difference = (int(coordsX-currentCoords[0]),int(coordsY-currentCoords[1]))
        if difference in self.validKnightMoves:
            return True
        print (difference,self.validKnightMoves)
        return False
    
knights_tour(7)
# Challenge 3
#%%
"""
Write a GUI n Qt Designer where a user can input a quadratic function y(x) = ax2 + bx + c, and then
it plots the parabola, indicating and labeling the roots. The user can choose a color for the parabola
and the roots.
"""
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalFrame = QtGui.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(80, 40, 341, 401))
        self.verticalFrame.setObjectName(_fromUtf8("verticalFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalFrame)
        self.label.setMinimumSize(QtCore.QSize(323, 87))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.verticalFrame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.a = QtGui.QLineEdit(self.verticalFrame)
        self.a.setObjectName(_fromUtf8("a"))
        self.horizontalLayout_2.addWidget(self.a)
        self.label_5 = QtGui.QLabel(self.verticalFrame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_2.addWidget(self.label_5)
        self.b = QtGui.QLineEdit(self.verticalFrame)
        self.b.setObjectName(_fromUtf8("b"))
        self.horizontalLayout_2.addWidget(self.b)
        self.label_6 = QtGui.QLabel(self.verticalFrame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.c = QtGui.QLineEdit(self.verticalFrame)
        self.c.setObjectName(_fromUtf8("c"))
        self.horizontalLayout_2.addWidget(self.c)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(self.verticalFrame)
        self.label_7.setMinimumSize(QtCore.QSize(323, 0))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(self.verticalFrame)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.equation = QtGui.QLineEdit(self.verticalFrame)
        self.equation.setObjectName(_fromUtf8("equation"))
        self.horizontalLayout.addWidget(self.equation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Red = QtGui.QRadioButton(self.verticalFrame)
        self.Red.setObjectName(_fromUtf8("Red"))
        self.Parabola = QtGui.QButtonGroup(MainWindow)
        self.Parabola.setObjectName(_fromUtf8("Parabola"))
        self.Parabola.addButton(self.Red)
        self.verticalLayout_3.addWidget(self.Red)
        self.Green = QtGui.QRadioButton(self.verticalFrame)
        self.Green.setObjectName(_fromUtf8("Green"))
        self.Parabola.addButton(self.Green)
        self.verticalLayout_3.addWidget(self.Green)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.label_3 = QtGui.QLabel(self.verticalFrame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Black = QtGui.QRadioButton(self.verticalFrame)
        self.Black.setObjectName(_fromUtf8("Black"))
        self.Root = QtGui.QButtonGroup(MainWindow)
        self.Root.setObjectName(_fromUtf8("Root"))
        self.Root.addButton(self.Black)
        self.verticalLayout_2.addWidget(self.Black)
        self.Blue = QtGui.QRadioButton(self.verticalFrame)
        self.Blue.setObjectName(_fromUtf8("Blue"))
        self.Root.addButton(self.Blue)
        self.verticalLayout_2.addWidget(self.Blue)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.graph = QtGui.QPushButton(self.verticalFrame)
        self.graph.setObjectName(_fromUtf8("graph"))
        self.verticalLayout.addWidget(self.graph)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Graph the parabola y(x) = ax^2 + bx + c</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">a</span></p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">b</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">c</span></p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">or</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">e.g. y1=x^2+2x+1</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Parabola</span></p></body></html>", None))
        self.Red.setText(_translate("MainWindow", "Red", None))
        self.Green.setText(_translate("MainWindow", "Green", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Root</span></p></body></html>", None))
        self.Black.setText(_translate("MainWindow", "Black", None))
        self.Blue.setText(_translate("MainWindow", "Blue", None))
        self.graph.setText(_translate("MainWindow", "Graph", None))

class PlotGui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(PlotGui,self).__init__(parent)
        self.setupUi(self)
        self.graph.clicked.connect(self.plotfnct)
 
    def plotfnct(self):
        a=0
        b=0
        c=0
        
        if self.a.text() == "" or self.b.text() == "" or self.c.text() == "":
            eq = list(self.equation.text().split("="))[1]
            if re.search(r'x\^',eq):
                a = int(re.search(r'[\.\d]+(?=x\^)',eq).group()) if re.search(r'[\.\d]+(?=x\^)',eq) else 1

            if re.search(r'x\+|x\-|x$',eq):
                b = int(re.search(r'[\.\d]+(?=x\+|x\-|x$)',eq).group()) if re.search(r'[\.\d]+(?=x\+|x\-|x$)',eq) else 1

            c = int(re.search(r'\+([\.\d]+)$',eq).group(1)) if re.search(r'\+([\.\d]+)$',eq) else 0
            
        else:
            a=float(self.a.text())
            b=float(self.b.text())
            c=float(self.c.text())
        graph = self.figure.add_subplot(111)
        graph.hold(False)
        root1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
        root2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
        x=np.arange(-np.pi,np.pi,.001)
        if root1>root2:
            x=np.arange(root2-4,root1+4,.001)
        else:
            x=np.arange(root1-4,root2+4,.001)
        y=a*x**2+b*x+c
        colorOfParabola = 'g' if self.Green.isChecked() else 'r'
        if self.Blue.isChecked():
            graph.plot(x,y,colorOfParabola,[root1,root2],[0,0], 'bo')
        else:
            graph.plot(x,y,colorOfParabola,[root1,root2],[0,0], 'ko')
        self.canvas.draw()
        
if __name__=='__main__':
    from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas)
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    import re
 
    app = QtGui.QApplication(sys.argv)
    main = PlotGui()
    main.show()
    sys.exit(app.exec_())
