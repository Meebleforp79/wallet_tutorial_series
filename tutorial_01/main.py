#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import json

################################################################################
#Source: https://github.com/jgarzik/python-bitcoinrpc.git
################################################################################
from bitcoinrpc.authproxy import AuthServiceProxy


################################################################################
#Configuration: information from ~/.bitcoin/bitcoin.conf to connect to bitcoind
################################################################################
class Configuration():
    def __init__(self):
        self.protocol = "http"
        self.username = "rpc_username" #Change this to match your ~/.bitcoin/bitcoin.conf
        self.password = "rpc_password" #Change this to match your ~/.bitcoin/bitcoin.conf
        self.ip       = "localhost"
        self.port     = "8332"
    
    ############################################################################
    #Description: This is the uri used to connect to bitcoind
    #Parameters: none
    #Return value: string
    ############################################################################
    def get_uri(self):
        self.uri = self.protocol+"://"+self.username+":"+self.password+"@"+self.ip+":"+self.port
        return self.uri

################################################################################
#Command: Send commands to bitcoind and fetch results
################################################################################
class Command():
    def __init__(self):
        self.conf = Configuration()
        self.access = AuthServiceProxy(self.conf.get_uri())
    
    ############################################################################
    #Retrieves bitcoind getinfo
    #Parameters: none
    #Return value: list
    ############################################################################
    def get_info(self):
        self.info = self.access.getinfo()
        return self.info
    
    ############################################################################
    #Retrieves bitcoind list_accounts
    #Parameters: none
    #Return value: list
    ############################################################################
    def list_accounts(self):
        self.info = self.access.listaccounts()
        return self.info

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
#Program entry point
################################################################################
def main():
    app = QtGui.QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

