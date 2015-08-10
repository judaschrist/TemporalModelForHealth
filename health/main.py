# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'

from data.diagnosis import read_diagnosis_from_file

pdict = read_diagnosis_from_file('F:\\PUPH-data\\diagnosis.csv')
print(len(pdict))
print(sum([len(pdict[key]) for key in pdict]))

codes = [[dia.name for dia in pdict[key]] for key in pdict]
# print(codes[0][1].decode('utf-8'))

from gensim import corpora
codedict = corpora.Dictionary(codes)

corpus = [codedict.doc2bow(codesperson) for codesperson in codes]


from gensim.models.ldamodel import LdaModel
from gensim.models.ldamulticore import LdaMulticore
print("start inferring...single")
import time
start_time = time.time()
ldaSingle = LdaModel(corpus, 20)
print("--- %s seconds ---" % (time.time() - start_time))
print("start inferring...multi")
start_time = time.time()
ldamulti = LdaMulticore(corpus, 20)
print("--- %s seconds ---" % (time.time() - start_time))
topics = ldaSingle.show_topics(formatted=False, num_topics=20)

count = 0
for wordlist in topics:
    count += 1
    print('topic ' + str(count))
    for wordturple in wordlist:
        print('\t' + codedict.__getitem__(int(wordturple[1])) + str(wordturple[0]))


