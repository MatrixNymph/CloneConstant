#!/usr/bin.env python

class CFGReader:
    """ All things to do with configuration of Juke """
    def __init__(self, fileLoc):
        self.fileLoc = fileLoc
    
    def readCfg(self, specCfg):
        #Read file
        cfgFile = open(self.fileLoc, 'r')
        with cfgFile as f:
            content = f.readlines()
        cfgFile.close()

        #Search for requested cfg
        for each in content:
            if specCfg in each:
               return each.split('\'')[1]

