#!/usr/bin/env python

from Filesystem import *
from CFGReader import *

import HashCheck
import shutil
import sys
import os

# Read Clone.cfg
cfg = CFGReader('Clone.cfg')
src_dir = cfg.readCfg('src_dir')
dst_dir = cfg.readCfg('dst_dir')

# Check if destination folder exists
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Enumerate files
src_fs = Filesystem(src_dir)
src_files = src_fs.enum()

dst_fs = Filesystem(dst_dir)
dst_files = dst_fs.enum()

# Prepare filenames for comparison
src_stripped = []
dst_stripped = []

for filename in src_files:
    src_stripped.append([filename, filename[len(src_dir):len(filename)]])
for filename in dst_files:
    dst_stripped.append([filename, filename[len(dst_dir):len(filename)]])

# Compare filesystems
newFiles = []
changedFiles = []
delFiles = []

for src_file in src_stripped:
    in_list = 0
    for dst_file in dst_stripped:
        if src_file[1] == dst_file[1]:
            in_list = 1
            if not HashCheck.compareMD5(HashCheck.fileMD5(src_file[0]), HashCheck.fileMD5(dst_file[0])):
                changedFiles.append([src_file[0], dst_file[0]])
    if in_list == 0:
        newFiles.append(src_file)

for dst_file in dst_stripped:
    in_list = 0
    for src_file in src_stripped:
        if dst_file[1] == src_file[1]:
            in_list = 1
    if in_list == 0:        
        delFiles.append(dst_file)

print(newFiles)
print(changedFiles)
print(delFiles)

# Write file changes
for file in newFiles:
    shutil.copyfile(file[0], dst_dir + file[1])

for file in changedFiles:
    os.remove(os.path.join(dst_dir, file[1]))
    shutil.copyfile(file[0], os.path.join(dst_dir, file[1]))

for file in delFiles:
    os.remove(file[0])
