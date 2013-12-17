#!/usr/bin/env python

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

def compareMD5(hash1, hash2):
    return (hash1 == hash2)

