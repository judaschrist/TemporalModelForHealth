# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'
import os


def read_diagnosis_from_file(filepath):
    pdict = dict()
    f = open(filepath, 'r')
    count = 0
    for line in f:
        if count % 1000 == 0:
            print(str(count) + ' lines read...')
        if count > 5000000:
            break
        # line = f.readline()
        # print line.decode('utf-8')
        items = line.split(',')
        d = Diagnosis(items[4], items[5], items[6])
        pdict[items[0]] = pdict.get(items[0], [])
        pdict[items[0]].append(d)
        count += 1
    return pdict



class Diagnosis:
    def __init__(self, code, name, is_main):
        self.code = code
        self.name = name
        self.isMain = is_main

    pass
