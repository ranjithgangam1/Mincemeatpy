#!/usr/bin/env python
import mincemeat
import argparse


parser = argparse.ArgumentParser(usage="%(prog)s [options] server_name")
parser.add_argument("filename",help="File path")
parser.parse_args()
args = parser.parse_args()
file = open(args.filename,'r')
data = list(file)
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
    print v
    yield 'mathstats', int(v)

def reducefn(k, vs):
    add = sum(vs)
    length =len(vs)
    mean = add / length
    std_int =0
    for i in range(0, len(vs),1):
        std_int += ((vs[i]-mean)**2)
    std = (std_int/length)**(0.5)
    result = {'count':len(vs),'sum':add,'std':std}
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print 'count:', results['mathstats']['count']
print 'sum:', results['mathstats']['sum']
print 'Std. Dev:', results['mathstats']['std']
