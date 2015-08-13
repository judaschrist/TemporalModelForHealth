# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'

import codecs
import math

def testlda(corpus, id2token):
    from gensim.models.ldamodel import LdaModel
    from gensim.models.ldamulticore import LdaMulticore
    print("start inferring...single")
    import time
    start_time = time.time()
    ldaSingle = LdaModel(corpus, 20, id2word=id2token)
    print("--- %s seconds ---" % (time.time() - start_time))
    # print("start inferring...multi")
    # start_time = time.time()
    # ldamulti = LdaMulticore(corpus, 20)
    # print("--- %s seconds ---" % (time.time() - start_time))
    topics = ldaSingle.show_topics(formatted=False, num_topics=-1)
    # print(topics)
    count = 0
    for wordlist in topics:
        count += 1
        print('topic ' + str(count))
        for wordturple in wordlist:
            print('\t' + wordturple[1] + '\t' + str(wordturple[0]))


def testhlda(corpus, id2token):
    from gensim.models.hdpmodel import HdpModel
    hdp = HdpModel(corpus, id2token)
    # print hdp.show_topics(-1, 5, formatted=False)
    print(hdp.date)
    pass

def print_time_slice_doc_data(docslices, path, name='dia'):
    f = open(path + name + '-seq.dat', 'w')
    f.write(str(len(docslices)) + '\n')
    alldocs = []
    for docs in docslices:
        f.write(str(len(docs)) + '\n')
        alldocs += [docs[key] for key in docs]
    f.close()
    # print(alldocs)
    from gensim import corpora
    codedict = corpora.Dictionary(alldocs)
    corpus = [codedict.doc2bow(doc) for doc in alldocs]
    id2token = dict((v, k) for k, v in codedict.token2id.iteritems())
    f = open(path + name + '-mult.dat', 'w')
    for doc in corpus:
        f.write(str(len(doc)))
        for word, count in doc:
            f.write(' ' + str(word) + ':' + str(count))
        f.write('\n')
    f.close()
    f = codecs.open(path + name + '-dict.dat', 'w', 'utf-8')
    for key in id2token:
        # print id2token[key]
        print >> f, str(key) + " " + id2token[key]
    f.close()

def print_dtm_results(modelname, path, ntopicword=10):
    f = open(path + modelname + '\\lda-seq\\info.dat', 'r')
    info = [int(line.split()[1]) for line in f]
    numtopic = info[0]
    numterm = info[1]
    numslices = info[2]
    #read dict
    f = codecs.open(path + modelname + '-dict.dat', 'r', 'utf-8')
    termdict = [line.split()[1] for line in f]
    for ntopic in range(0, numtopic):
        f = open(path + modelname + '\\lda-seq\\topic-%03d-var-e-log-prob.dat'%ntopic, 'r')
        problist = [math.pow(math.e, float(line)) for line in f]
        f = codecs.open(path + modelname + '\\lda-seq\\t-%03d-show.dat'%ntopic, 'w', 'utf-8')
        for nslice in range(0, numslices):
            wordprob = {}
            for nterm in range(0, numterm):
                wordprob[nterm] = problist[numslices*nterm + nslice]
            topicword = [(termdict[word], wordprob[word]) for word in sorted(wordprob, key=wordprob.get, reverse=True)]
            print >> f, "time" + str(nslice)
            for word, prob in topicword[:10]:
                print >> f, '\t' + word + ' ' + str(prob)
        f.close()
