#!/usr/bin/env python

import os
import sys

class Filesystem:
    def __init__(self, *args):
        if len(args) == 1:
            self.__setup1__(*args)
        elif len(args) == 2:
            self.__setup2__(*args)

    def __setup1__(self, src_dir):
        self.src_dir = src_dir
        self.blacklist = []

    def __setup2__(self, src_dir, bFile):
        self.src_dir = src_dir
        self.blacklist = []
        inFile = open('blacklist.dat', 'r')

        # Read blacklist
        for entry in inFile:
            self.blacklist.append(entry)
            
    def enum(self):
        fileList = []

        for dirname, dirnames, filenames in os.walk(self.src_dir):
            # print path to all filenames.
            for filename in filenames:
                if not (filename in self.blacklist):
                    fileList.append(os.path.join(dirname, filename))

        return fileList

    def compare(self, src_fs, dst_fs):
        list1 = src_fs.enum()
        list2 = dst_fs.enum()
