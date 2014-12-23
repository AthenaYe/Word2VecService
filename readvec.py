#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import struct
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def readvec(vecname, max_words=2**32):
    lex = {}

    with open(vecname, 'rb') as f:
        words, size = map(int, f.readline().strip().split())

        print words, size
        for l in xrange(np.min((words, max_words))):
            if l % 10000 == 0:
                print "%.2f%%" % (float(l) / words * 100)
            flag = 0
            w = ''
            while 1:
                i = f.read(1)

                if i in ('\0', '\t', ' ', '\n'):
                    break

                w = w + i

            try:
                w = w.decode('utf-8')
            except Exception, e:
                print e
                flag = 1
                print l, w
                # print 'a'+w+'daaa'
                # print c
            vector = struct.unpack('<{}f'.format(size), f.read(4*size))

            f.read(1)
            if flag == 1:
                continue

            lex[w] = np.array(vector)

    return lex

if __name__ == '__main__':
    lex = readvec('vec2.bin')
    # print lex


# vim: ts=4 sw=4 sts=4 expandtab
