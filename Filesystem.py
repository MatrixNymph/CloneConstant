#!/usr/bin/env python

import os
import sys

class Filesystem:
    def __init__(self, rDir):
        self.rDir = rDir

    def __init__(self, rDir, bFile):
        self.rDir = rDir
        self.blacklist = []
        inFile = open('blacklist.dat', 'r')

        # Read blacklist
        for entry in inFile:
            self.blacklist.append(entry)
            
    def enum(self):
        fileList = []

        for dirname, dirnames, filenames in os.walk(self.rDir):
            # print path to all filenames.
            for filename in filenames:
                if filename in self.blacklist:
                    fileList.append(os.path.join(dirname, filename))

        return fileList
