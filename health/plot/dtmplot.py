# -*- coding: utf-8 -*-
__author__ = 'Lingxiao'

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import codecs
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# matplotlib.rc('font', )
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# print t
#
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--')
# plt.plot(t, t*2, 'r--')
# plt.show()


def print_dtm_plot(modelname, path, ntopicword=10, chartsize=(10, 5), nrowchart=1):
    f = open(path + modelname + '\\lda-seq\\info.dat', 'r')
    info = [int(line.split()[1]) for line in f]
    numtopic = info[0]
    numterm = info[1]
    numslices = info[2]

    # set chart sizes
    # fig = plt.gcf()
    # plt.figure(figsize=(20, 5))
    plt.figure(figsize=(nrowchart*chartsize[0], ((numtopic+nrowchart-1)/nrowchart)*chartsize[1]))
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=1, hspace=1)
    #read dict
    f = codecs.open(path + modelname + '-dict.dat', 'r', 'utf-8')
    termdict = [line.split()[1] for line in f]
    for ntopic in range(0, numtopic):
        f = open(path + modelname + '\\lda-seq\\topic-%03d-var-e-log-prob.dat'%ntopic, 'r')
        problist = [math.pow(math.e, float(line)) for line in f]
        print ntopic
        topicwordproblist = {}
        wordmaxlist = {}
        for nterm in range(0, numterm):
            wordtimelist = []
            word = termdict[nterm]
            for nslice in range(0, numslices):
                wordtimelist.append(problist[numslices*nterm + nslice])
            wordmaxlist[word] = max(wordtimelist)
            topicwordproblist[word] = wordtimelist
        chartlist = [(word, topicwordproblist[word]) for word in
                     sorted(wordmaxlist, key=wordmaxlist.get, reverse=True)[:ntopicword]]
        # print topicinplotlist
        plt.subplot((numtopic+nrowchart-1)/nrowchart, nrowchart, ntopic+1)
        plt.title(chartlist[0][0], fontproperties=font)
        for word, wordproblist in chartlist:
            plt.plot(wordproblist,  label=word)
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop=font)

    # fig.savefig(modelname, dpi=100)
    plt.show()
