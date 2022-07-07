import pandas as pd
from krit_creator import Krit

def get_krit(query):

    df = pd.read_csv('कृत्.csv')

    for ii in query:
        df = df[df['उपदेश'] == query]
    
    idx = df.index.values[0]

    with open('कृत्.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')

    if query in list(df['उपदेश']):
        return Krit(s[idx])

if __name__ == '__main__':

    print(get_krit('क्विप्'))