#!/usr/bin/env python
import mincemeat
import argparse
import itertools
import datetime
start_time = datetime.datetime.now()

parser = argparse.ArgumentParser(usage="%(prog)s [options] server_name")
parser.add_argument("filename",help="File path")
parser.parse_args()
args = parser.parse_args()


data = args.filename

print 'Attacking:', data



char_list = "abcdefghijklmnopqrstuvwxyz0123456789"

word_1=[''.join(i) for i in itertools.product(char_list, repeat= 1)]
word_2=[''.join(i) for i in itertools.product(char_list, repeat= 2)]
word_3=[''.join(i) for i in itertools.product(char_list, repeat= 3)]
word_4=[''.join(i) for i in itertools.product(char_list, repeat= 4)]

datasource = {data:[word_1,word_2,word_3,word_4]}


def mapfn(k, v):
    import hashlib, md5
    match =[]
    for each in v:
        for each1 in each:
            hash_object = hashlib.md5(each1)
            ltd_5 = hash_object.hexdigest()[:5]
            if ltd_5 == k:
               match.append(each1)
    yield 'Found',match


def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

print 'Time in hh:mm:ss format'
print datetime.datetime.now()-start_time