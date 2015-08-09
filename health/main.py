# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'

from data.diagnosis import read_diagnosis_from_file

pdict = read_diagnosis_from_file('c:\\Users\\Lingxiao\\Desktop\\diagnosis.csv')
print(len(pdict))
print(sum([len(pdict[key]) for key in pdict]))

codes = [[dia.name for dia in pdict[key]] for key in pdict]
# print(codes[0][1].decode('utf-8'))

from gensim import corpora
codedict = corpora.Dictionary(codes)

corpus = [codedict.doc2bow(codesperson) for codesperson in codes]

print("start inferring...20")
from gensim.models.ldamodel import LdaModel
lda = LdaModel(corpus, num_topics=20)
topics = lda.show_topics(formatted=False, num_topics=20)

count = 0
for wordlist in topics:
    count += 1
    print('topic ' + str(count))
    for wordturple in wordlist:
        print('\t' + codedict.__getitem__(int(wordturple[1])) + str(wordturple[0]))


