
import numpy as np
import os

src = '/root/dispnet/TimeCycle/DATA/manifest.txt'
outlist = '/root/dispnet/TimeCycle/DATA/vlog_frames_12fps.txt'
foldername = '/root/dispnet/TimeCycle/DATA/vlog_frames_12fps/'

file = open(src, 'r')
fout = open(outlist, 'w')

for line in file:
    line = line[:-1]
    fname = foldername + line
    fnms  = len(os.listdir(fname))

    outstr = fname + ' ' + str(fnms) + '\n'
    fout.write(outstr)


file.close()
fout.close()
