#!/usr/bin/env python

from Filesystem import *

import hashlib

def fileMD5(filename):
    block_size = 2**20
    f = open(filename)
    md5 = hashlib.md5()

    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)

    f.close()
    return md5.digest()

def dirMD5(src_dir, dst_dir):
    block_size = 2**20

    # Enumerate files
    src_fs = Filesystem(src_dir)
    src_files = src_fs.enum()

    dst_fs = Filesystem(dst_dir)
    dst_files = dst_fs.enum()

    # Prepare filenames for comparison
    src_prefix = os.path.commonprefix(src_files)
    dst_prefix = os.path.commonprefix(dst_files)

    src_stripped = []
    dst_stripped = []

    for filename in src_files:
        src_stripped.append([filename, filename.strip(src_prefix)])
    for filename in dst_files:
        dst_stripped.append([filename, filename.strip(dst_prefix)])

    # Compare src to dst
    for each in src_stripped:
        if not each in dst_stripped:
            return False
 
    # Compare dst to src
    for each in dst_stripped:
        if not each in dst_stripped:
            return False

    # Compare hashes
    for each in src_stripped:
        s_f = open(os.path.join(src_prefix + each))
        d_f = open(os.path.join(dst_prefix + each))
	s_md5 = hashlib.md5()
        d_md5 = hashlib.md5()

        while True:
            s_data = s_f.read(block_size)
            d_data = s_f.read(block_size)
            if not s_data:
                print('break')
                break
            if not d_data:
                print('break')
                break
            s_md5.update(s_data)
            d_md5.update(d_data)
            s_f.close()
            d_f.close()
            if s_md5.digest() == d_md5.digest():
                return True
            else:
                return False

def compareMD5(hash1, hash2):
    return (hash1 == hash2)

