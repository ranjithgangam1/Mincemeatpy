#!/usr/bin/env python

import mincemeat
import datetime

start_time = datetime.datetime.now()
data=[]
for i in range (2, 10000000, 5000):
    data.append(range(i,i+50000))
datasource = dict(enumerate(data))

def mapfn(k, v):
    for line in v:
        vs_str=str(line)
        if vs_str==vs_str[::-1]:
            yield "Prime_and_palindrome ",int(vs_str)

def reducefn(k, vs):
    import math
    prime_pal =[2,3]
    for pal in vs:
        prm=1
        for i in range(2,int(math.sqrt(pal)+1)):
            if pal % i == 0:
                prm=0
                break
        if prm:
            prime_pal.append(pal)
    return prime_pal

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

print 'Time in hh:mm:ss format'
print datetime.datetime.now()-start_time