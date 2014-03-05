#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from bitcoinrpc.authproxy import AuthServiceProxy
import json

class Configuration():
    def __init__(self):
        self.protocol	= "http"
        self.username	= "rpc_username"
        self.password	= "rpc_password"
        self.ip			= "localhost"
        #self.port		= "18332"
        self.port		= "8332"
    
    def get_uri(self):
        self.uri = self.protocol+"://"+self.username+":"+self.password+"@"+self.ip+":"+self.port
        return self.uri

class Command():
    def __init__(self):
        self.conf = Configuration()
        self.access = AuthServiceProxy(self.conf.get_uri())
    
    def get_info(self):
        #self.info = self.access.getinfo()
        self.info = self.access.listaccounts()
        return self.info

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
    app = QtGui.QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

