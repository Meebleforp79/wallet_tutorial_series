#!/usr/bin/python
# -*- coding: utf-8 -*-

from bitcoinrpc.authproxy import AuthServiceProxy
from configuration import *

class Command():
    def __init__(self):
        self.configuration = Configuration("bitcoin")
        self.access = AuthServiceProxy(self.configuration.get_uri())
    
    def get_info(self):
        self.info = self.access.getinfo()
        #self.info = self.access.listaccounts()
        return self.info

def main():
    exit()

if __name__ == '__main__':
    main()
