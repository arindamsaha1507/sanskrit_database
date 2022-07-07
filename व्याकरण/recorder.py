from vinyaasa import *

def start_recording(fname):
    ff = open(fname, 'w')
    ff.write('| स्थिति | सूत्र | टिप्पणी |\n| ----- | ------- | ------ |\n')
    return ff


def record(ff, स्थिति, सूत्र, टिप्पणी):
    ff.write('| {} | {} | {} |\n'.format(get_shabda(स्थिति), सूत्र, टिप्पणी))

def end_recording(ff):
    ff.close()