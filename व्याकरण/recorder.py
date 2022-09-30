from vinyaasa import *

def start_recording(fname):
    ff = open(fname, 'w')
    ff.write('स्थिति, सूत्र, टिप्पणी\n')
    return ff


def record(fname, s, t, r):
    ff = open(fname, 'a')
    print(s)
    ff.write(s + ', ' + t + ', ' + r +'\n')
    ff.close()

def end_recording(ff):
    ff.close()