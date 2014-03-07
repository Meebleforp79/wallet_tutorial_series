#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#Source: https://github.com/jgarzik/python-bitcoinrpc.git
################################################################################
from bitcoinrpc.authproxy import AuthServiceProxy

from configuration import *

################################################################################
#Command: Send commands to bitcoind and fetch results
################################################################################
class Command():
    def __init__(self):
        #CHANGED: Configuration() has been changed to accept types of altcoins
        self.configuration = Configuration("bitcoin")
        self.access = AuthServiceProxy(self.configuration.get_uri())
    
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
#Command entry point
################################################################################
def main():
    exit()

if __name__ == '__main__':
    main()
