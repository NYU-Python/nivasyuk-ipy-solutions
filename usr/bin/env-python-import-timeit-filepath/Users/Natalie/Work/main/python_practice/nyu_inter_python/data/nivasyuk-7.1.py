#!/usr/bin/env python

import timeit

filepath = '/Users/Natalie/Work/main/python_practice/nyu_inter_python/data/words.txt'
fh = open(filepath)

def forloop(fh):

    resultlist = []

    lines = fh.readlines()

    for line in lines:
        clean_word = line.lower().strip('.,:;!?\n')
        resultlist.append(clean_word)

    return resultlist


def listcomp(fh):

    lines = fh.readlines()

    resultlist = [line.lower().strip('.,:;!?\n') for line in lines]

    return resultlist


def gencomp(fh):

    lines = fh.readlines()

    resultgen = (line.lower().strip('.,:;!?\n') for line in lines)

    return resultgen

def mapfunc(fh):

    lines = fh.readlines()

    resultlist = map(lambda line: line.lower().strip('.,:;!?\n'), lines)

    return resultlist


def main():

    #res = gencomp(fh)
    #print list(res)[:20]

    forlooptime = timeit.timeit('forloop(fh)', setup='from __main__ import forloop, fh', number=100)
    listcomptime = timeit.timeit('listcomp(fh)', setup='from __main__ import listcomp, fh', number=100)
    gencomptime = timeit.timeit('gencomp(fh)', setup='from __main__ import gencomp, fh', number=100)
    mapfunctime = timeit.timeit('mapfunc(fh)', setup='from __main__ import mapfunc, fh', number=100)

    print "for-loop time: \t\t\t\t {0}".format(forlooptime)
    print "list comprehension time: \t {0}".format(listcomptime)
    print "generator comprehension time:{0}".format(gencomptime)
    print "map function time: \t\t\t {0}".format(mapfunctime)


if __name__ == "__main__":

    main()