#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      illuz <iilluzen[at]gmail.com>
# File:        timestamp-generator.py
# Create Date: 2015-05-20 10:50:12
# Usage:       timestamp-generator.py 
# Descripton:  generate unix-timestamp

import sys
from datetime import datetime

usage = 'generate unix-timestamp'
formt = 'timestamp-generator.py year month start-day end-day [interval = 1]'
hint  = 'timestamp-generator.py 2015 6 12 18 1'

def generate(argv):
    y, m, sd, ed, it = map(int, argv)
    for i in range(sd, ed):
        dt = datetime(y, m, i)
        print(str(dt) + ' is ' + dt.strftime("%s"))

def main():
    if 5 <= len(sys.argv) <= 6:
        argv = sys.argv
        if (len(argv) == 5):
            argv.append(1)
        generate(argv[1:])
    else:
        print('Wrong Parameter!')
        print('Usage: ' + usage)
        print('Format: ' + formt)
        print('Hint: ' + hint)

if __name__ == '__main__':
    main()

