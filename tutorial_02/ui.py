#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from command import *

class UI(QtGui.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.init_ui()
    
    def init_ui(self):
        command = Command()
        info = command.get_info()
        
        keys = info.keys()
        
        label = []
        line_edit = []
        
        for (i, key) in enumerate(keys):
            label.append(QtGui.QLabel(str(keys[i])))
            line_edit.append(QtGui.QLineEdit(str(info[keys[i]])))
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        for (i, item) in enumerate(label):
            grid.addWidget(label[i], i, 0)
            grid.addWidget(line_edit[i], i, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('getinfo')
        self.show()

def main():
    exit()

if __name__ == '__main__':
    main()
