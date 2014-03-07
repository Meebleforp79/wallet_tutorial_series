#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from command import *

################################################################################
#Create the User Interface
################################################################################
class UI(QtGui.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.init_ui()
    
    ############################################################################
    #Creates the window and widgets
    #Parameters: none
    #Return value: none
    ############################################################################
    def init_ui(self):
        #Create a command object to communicate to bitcoind
        command = Command()
        #send a bitcoind getinfo request and retrieve information
        info = command.get_info()
        
        keys = info.keys()
        
        label = []
        line_edit = []
        
        #create label and line edit widgets for items in info based on keys
        for (i, key) in enumerate(keys):
            label.append(QtGui.QLabel(str(keys[i])))
            line_edit.append(QtGui.QLineEdit(str(info[keys[i]])))
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        
        #place label and line edit widgets on the UI grid
        for (i, item) in enumerate(label):
            grid.addWidget(label[i], i, 0)
            grid.addWidget(line_edit[i], i, 1)
        
        self.setLayout(grid) 
        
        #create window
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('getinfo')
        self.show()

################################################################################
#UI entry point
################################################################################
def main():
    exit()

if __name__ == '__main__':
    main()
