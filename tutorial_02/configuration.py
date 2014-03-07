#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

################################################################################
#Configuration: information from ~/.bitcoin/bitcoin.conf to connect to bitcoind
#Parameters: string altcoin I.E. "bitcoin", "litecoin", etc.
################################################################################
class Configuration:
    def __init__(self, altcoin):
        self.altcoin       = altcoin
        self.directory     = "/home/"+os.getenv('USER')+"/."+altcoin+"/"
        self.protocol      = "http"
        self.configuration = self.read()
    
    ############################################################################
    #Description: This is the uri used to connect to bitcoind
    #Parameters: none
    #Return value: string
    ############################################################################
    def get_uri(self):
        self.uri = self.protocol+"://"+self.configuration["rpcuser"]+":"+self.configuration["rpcpassword"]+"@"+self.configuration["rpcconnect"]+":"+self.configuration["rpcport"]
        return self.uri
    
    ############################################################################
    #Description: reads the ~/.bitcoin/bitcoin.conf file
    #Parameters: none
    #Return value: dictionary
    ############################################################################
    def read(self):
        from ConfigParser import SafeConfigParser
        
        class Fake_Head(object):
            def __init__(self, fp):
                self.fp = fp
                self.sechead = '[all]\n'
            def readline(self):
                if self.sechead:
                    try: return self.sechead
                    finally: self.sechead = None
                else:
                    s = self.fp.readline()
                    if s.find('#') != -1:
                        s = s[0:s.find('#')].strip() +"\n"
                    return s
        
        config_parser = SafeConfigParser()
        config_parser.readfp(Fake_Head(open(os.path.join(self.directory, self.altcoin+".conf"))))
        return dict(config_parser.items("all"))

################################################################################
#Configuration entry point
################################################################################
def main():
    exit()

if __name__ == '__main__':
    main()

