__author__ = 'Lingxiao'


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
    # count = 0
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
