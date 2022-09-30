import pandas as pd
from dhaatu_creator import Dhaatu
import yaml
from pathlib import Path

def get_dhaatu(query, find_unique=False):

    df = pd.read_csv('धातु.csv')

    for ii in query.keys():
        if ii in df.columns:
            df = df[df[ii] == query[ii]]
    
    idx = df.index.values

    with open('धातुपाठ_मूल.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')
    
    return [Dhaatu(s[ii]) for ii in idx]


if __name__ == '__main__':

    query = yaml.safe_load(Path('input.yml').read_text())
    
    d = get_dhaatu(query)

    for x in d:
        print(x)
        print()
