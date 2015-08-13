# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'
import os


def read_diagnosis_from_file(filepath):
    pdict = dict()
    f = open(filepath, 'r')
    count = 0
    for line in f:
        if count % 100000 == 0:
            print(str(count) + ' lines read...')
        if count > 500000:
            break
        # line = f.readline()
        # print line.decode('utf-8')
        items = line.split(',')
        d = Diagnosis(items[4], items[5], items[6])
        pdict[items[0]] = pdict.get(items[0], [])
        pdict[items[0]].append(d)
        count += 1
    return pdict

def read_dia_sliced_by_age(filepath, sliceage=5, startage=40, endage=99):
    '''以5岁为界，从40岁开始，将诊断记录组织成年龄排序的方式'''
    f = open(filepath, 'r')
    count = 0
    # docslices = [{}]*((endage-startage)/5 + 1)
    docslices = [{} for n in range(startage, endage + 1, sliceage)]
    for line in f:
        if count % 100000 == 0:
            print(str(count) + ' lines read...')
        if count > 1000000:
            break
        count += 1
        items = line.split(',')
        pid = items[0]
        dname = items[2]
        try:
            age = int(items[-2])
        except:
            print count
            continue
        if age < startage:
            continue
        if age > endage:
            age = endage
        numslice = (age-startage)/5
        doc = docslices[numslice].get(pid, [])
        doc.append(dname)
        docslices[numslice][pid] = doc
    return docslices




class Diagnosis:
    def __init__(self, code, name, is_main):
        self.code = code
        self.name = name
        self.isMain = is_main

    pass
