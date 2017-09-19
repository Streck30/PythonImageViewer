#!/usr/bin/python3

"""
Fall 2017 CSc 690 

File: Browser Warmup
This example shows how to open a display window

Author: Andrew Streckfus
Last edited: 9/4/17
"""

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class Window(QWidget):
 
    def __init__(self,width,height,border):
        super().__init__()
        self.height = height
        self.width = width
        self.border = border
        self.index = 0
        self.leftBreak = 0
        self.rightBreak = 4
        self.bigPixList = []
        self.pixList = []
        self.label = []
        self.bigLabel = QLabel(self)
        self.bigLabel.resize(700,500)
        self.bigLabel.move(50,50)
        self.bigLabel.hide()
        self.mode = 0
        self.initUI()
 
    def initUI(self):
        # title of window
        self.setWindowTitle('PyQt5 Main Window')
        # place window on screen at x=0, y=0
        self.setGeometry(0, 0, self.width, self.height)
        self.setStyleSheet('background-color: black')
        #sets up QLabels for later input
        for i in range(0, 5, 1):
            self.label.append(QLabel(self))
            self.label[i].move(self.border +i*100+50*i, self.border)
            self.label[i].resize(100, 100)
            self.label[i].setStyleSheet('background-color: red')
            if(i == 0):
                self.label[i].setStyleSheet('background-color: blue')
        #places pictures into pixmap array
        i = 0
        for file in os.listdir('data'):
            self.pixList.append(QPixmap(os.path.join('data', file)))
            self.bigPixList.append(QPixmap(os.path.join('data',file)))
            if(self.pixList[i].height() > 90):
                self.pixList[i] = self.pixList[i].scaledToHeight(90)
            if(self.pixList[i].width() > 90):
                self.pixList[i] = self.pixList[i].scaledToWidth(90)
            if(self.bigPixList[i].width() > 700):
                self.bigPixList[i] = self.bigPixList[i].scaledToWidth(700)
            if(self.bigPixList[i].height() > 500):
                self.bigPixList[i] = self.bigPixList[i].scaledToHeight(500)
            i = i + 1
        self.bigLabel.setPixmap(self.bigPixList[0])
        #puts initial pixmaps into the designated qlabels
        for i in range(0, 5, 1):
            self.label[i].setPixmap(self.pixList[i])
            self.label[i].setAlignment(Qt.AlignCenter)
        self.show()
    #Moves the pointer to the picture one to the left.  If it breaks the bounds, it will move the frame
    def moveIndexLeft(self):
        j = 0
        self.label[self.index % 5].setStyleSheet('background-color:red')
        self.index = self.index - 1
        if(self.index < self.leftBreak):
            self.leftBreak = self.leftBreak - 5
            self.rightBreak = self.rightBreak - 5
            for i in range(self.leftBreak, 1 + self.rightBreak, 1):
                self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
                j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #Moves the pointer one picture to the right.  If it breaks the bounds of QLabel it will move the frame
    def moveIndexRight(self):
        j = 0
        self.label[self.index % 5].setStyleSheet('background-color: red')
        self.index = self.index + 1
        if(self.index > self.rightBreak):
            self.leftBreak = self.leftBreak + 5
            self.rightBreak = self.rightBreak + 5
            for i in range(self.leftBreak, 1 + self.rightBreak, 1):
                self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
                j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #Zooms in on the specific picture selected and puts it into a 700 x 500 frame    
    def zoomIn(self):
        self.mode = 1
        for i in range(0, 5, 1):
            self.label[i].hide()
        self.bigLabel.setAlignment(Qt.AlignCenter)
        self.bigLabel.show()
    #Goes back to default view
    def zoomOut(self):
        self.mode = 0
        self.bigLabel.hide()
        for i in range(0, 5, 1):
            self.label[i].show()
    #shifts the frame 5 pictures to the left
    def shiftLeft(self):
        self.label[self.index % 5].setStyleSheet('background-color:red')
        j = 0
        self.index = self.leftBreak - 1
        self.leftBreak = self.leftBreak - 5
        self.rightBreak = self.rightBreak - 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #shifts the frame 5 pictures to the right
    def shiftRight(self):
        self.label[self.index % 5].setStyleSheet('background-color: red')
        j = 0
        self.index = self.rightBreak + 1
        self.rightBreak = self.rightBreak + 5
        self.leftBreak = self.leftBreak + 5
        for i in range(self.leftBreak, 1 + self.rightBreak, 1):
            self.label[j].setPixmap(self.pixList[i % len(self.pixList)])
            j = j + 1
        self.label[self.index % 5].setStyleSheet('background-color: blue')
        self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
    #all of the key inputs and their responses in functions
    def keyPressEvent(self, event):
        if(event.key() == 16777234):
            self.moveIndexLeft()
        if(event.key() == 16777236):
            self.moveIndexRight()
        if(event.key() == 16777235):
            self.zoomIn()
        if(event.key() == 16777237):
            self.zoomOut()
        if(event.key() == 44):
            self.shiftLeft()
        if(event.key() == 46):
            self.shiftRight()
    def mousePressEvent(self, QMouseEvent):
        if(self.mode == 0):
            setPicTo = -1
            if(QMouseEvent.y() > 49 and QMouseEvent.y() < 151):
                if(QMouseEvent.x() > 49 and QMouseEvent.x() < 151):
                    setPicTo = 0
                if(QMouseEvent.x() > 199 and QMouseEvent.x() < 301):
                    setPicTo = 1
                if(QMouseEvent.x() > 349 and QMouseEvent.x() < 451):
                    setPicTo = 2
                if(QMouseEvent.x() > 499 and QMouseEvent.x() < 601):
                    setPicTo = 3
                if(QMouseEvent.x() > 649 and QMouseEvent.x() < 751):
                    setPicTo = 4
                if(setPicTo > -1):
                    self.label[self.index % 5].setStyleSheet('background-color:red')
                    self.mode = 1
                    self.index = self.leftBreak + setPicTo
                    self.label[self.index % 5].setStyleSheet('background-color:blue')
                    self.bigLabel.setPixmap(self.bigPixList[self.index % len(self.pixList)])
                    for i in range(0, 5, 1):
                        self.label[i].hide()
                    self.bigLabel.setAlignment(Qt.AlignCenter)
                    self.bigLabel.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    h = 600
    w = 800
    b = 50
    window = Window(w,h,b)
    sys.exit(app.exec_())
