# -*- coding: utf-8 -*-
from health.models import testlda, testhlda

__author__ = 'Lingxiao'

if __name__ == '__main__':

    from data.diagnosis import read_diagnosis_from_file

    pdict = read_diagnosis_from_file('C:\\Users\\Lingxiao\\Desktop\\diagnosis.csv')
    codes = [[dia.name for dia in pdict[key]] for key in pdict]
    # print(codes[0][1].decode('utf-8'))

    from gensim import corpora
    codedict = corpora.Dictionary(codes)
    corpus = [codedict.doc2bow(codesperson) for codesperson in codes]
    id2token = dict((v, k) for k, v in codedict.token2id.iteritems())

    # testlda(corpus, id2token)
    testhlda(corpus, id2token)

