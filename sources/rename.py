#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        rename.py
# Create Date: 2015-03-02 12:54:26
# Descripton:  rename


msg = """rename.py dir file startpos endpos [test]"""

import os, sys, re, fnmatch

def get_newfile(argv):
    """ return a list of tuple"""
    ret = []
    dir = argv[0]
    exp = argv[1]
    startpos = int(argv[2])
    endpos = int(argv[3])

    for root, dirs, files in os.walk(dir):
        for file in files:
            if re.search(exp, file):
                dot_pos = file.rfind('.')
                pre = file[:dot_pos]
                new_file = pre[startpos: endpos] + file[dot_pos:]
                ret.append((root+'/'+file, root+'/'+new_file))
                # print file + ' --> ', new_file
    return ret

def main():
    if len(sys.argv) != 5 and len(sys.argv) != 6:
        print 'Wrong Parameter!'
        print 'Usage:', msg 
    else:
        try:
            change_map = get_newfile(sys.argv[1:])
            if sys.argv[-1] == 'test':
                for i in change_map:
                    print i[0].decode('utf-8'), '-->', i[1].decode('utf-8')
            else:
                for i in change_map:
                    os.rename(i[0], i[1])
        except IOError:
            print "Open directory or file error!"
            pass

if __name__ == '__main__':
    main()
