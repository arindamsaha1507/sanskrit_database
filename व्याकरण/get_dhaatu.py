import pandas as pd
from dhaatu_creator import Dhaatu

def get_dhaatu(query, find_unique=False):

    df = pd.read_csv('धातु.csv')

    for ii in query.keys():
        df = df[df[ii] == query[ii]]
    
    idx = df.index.values

    with open('धातुपाठ_मूल.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')
    
    return [Dhaatu(s[ii]) for ii in idx]


if __name__ == '__main__':

    query = {
        'उपदेश': 'मी॒ञ्',
        # 'गण': 'भ्वादि',
        # 'उपदेश': 'गुपँ॒'
    }

    d = get_dhaatu(query)

    for x in d:
        print(x)
        print()