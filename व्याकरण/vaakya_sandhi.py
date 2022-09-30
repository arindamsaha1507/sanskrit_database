import pandas as pd
import yaml
from pathlib import Path

from pratyaahaara import expand_pratyahaara
from varna import *
from vinyaasa import get_shabda, get_vinyaasa
from sutra import *

def pada_sandhi(mm, df=None):

    fname = 'output.csv'

    if df is None:

        df = pd.DataFrame(columns=['स्थिति', 'सूत्र', 'टिप्पणी'])

    pada = mm.split(' ')

    assert len(pada) == 2

    primary = pada[0]        
    secondary = pada[1]

    row = {'स्थिति': mm, 'सूत्र': '-', 'टिप्पणी': '-'}
    df = df.append(row, ignore_index=True)

    pv = get_vinyaasa(primary)
    sv = get_vinyaasa(secondary)

    if pv[-1] in expand_pratyahaara('अच्'):
        if sv[0] in expand_pratyahaara('हल्'):
            pass
        else:
            if pv[-1] in expand_pratyahaara('एङ्') and sv[0] == 'अ':
                df = एङः_पदान्तादति(df)
            elif (pv[-1] == sv[0] and pv[-1] in expand_pratyahaara('अक्')) or (set((pv[-1], sv[0])) in [set(('अ', 'आ')), set(('इ', 'ई')), set(('उ', 'ऊ')), set(('ऋ', 'ॠ')), set(('ऋ', 'ऌ')), set(('ॠ', 'ऌ'))]):
                df = अकः_सवर्णे_दीर्घः(df)
            elif pv[-1] in ['अ', 'आ'] and sv[0] in expand_pratyahaara('एच्'):
                df = वृद्धिरेचि(df)
            elif pv[-1] in ['अ', 'आ'] and sv[0] in expand_pratyahaara('अक्'):
                df = आद्गुणः(df)
            elif pv[-1] in expand_pratyahaara('एच्') and sv[0] in expand_pratyahaara('अच्'):
                df = एचोऽयवायावः(df, pada=True)
            elif pv[-1] in expand_pratyahaara('इक्') and sv[0] in expand_pratyahaara('अच्'):
                df = इको_यणचि(df)
    else:
        if (primary == 'सस्' or primary == 'एषस्') and sv[0] in expand_pratyahaara('हल्') and secondary not in avasaana:
            df = एतत्तदोः_सुलोपोऽकोरनञ्समासे_हलि(df)
        elif pv[-1] == 'स्':
            df = ससजुषो_रुः(df)
            if secondary in avasaana:
                df = खरवसानयोर्विसर्जनीयः(df)
            else:
                if sv[0] in expand_pratyahaara('खर्'):
                    df = खरवसानयोर्विसर्जनीयः(df)
                else:
                    if pv[-2] == 'अ':
                        if sv[0] == 'अ':
                            df = अतो_रोरप्लुतादप्लुते(df)
                        elif sv[0] in expand_pratyahaara('हश्'):
                            df = हशि_च(df)
                        else:
                            df = भोभगोअघोअपूर्वस्य_योऽशि(df)
                    elif pv[-2] == 'आ':
                        df = भोभगोअघोअपूर्वस्य_योऽशि(df)
        
        else:
            if pv[-1] in expand_pratyahaara('झल्'):
                df = झलां_जशोऽन्ते(df)
            elif pv[-1] == 'र्' and (secondary in avasaana or sv[0] in expand_pratyahaara('खर्')):
                df = खरवसानयोर्विसर्जनीयः(df)
            elif secondary in avasaana:
                pass
            elif pv[-1] == 'म्' and secondary not in avasaana:
                if sv[0] in expand_pratyahaara('हल्'):
                    df = मोऽनुस्वारः(df)

            elif pv[-1] == 'न्' and sv[0] in expand_pratyahaara('छव्'):
                df = नश्छव्यप्रशान्(df)
            elif pv[-1] == 'न्' and sv[0] == 'ल्':
                df = तोर्लि(df)
            elif pv[-1] == 'न्' and sv[0] in ['श्', 'च्', 'छ्', 'ज्', 'झ्', 'ञ्']:
                df = स्तोः_श्चुना_श्चुः(df)

            elif pv[-1] in expand_pratyahaara('हल्') and sv[0] in expand_pratyahaara('अच्'):

                if pv[-1] in expand_pratyahaara('ङम्') and pv[-2] in ['अ', 'इ', 'उ', 'ऋ', 'ऌ']:
                    
                    df = ङमो_ह्रस्वादचि_ङमुण्नित्यम्(df)

    s = get_sthiti(df)
    s = get_vinyaasa(s)
    if ' ' in s:
        ii = s.index(' ')
        if s[ii-1] in expand_pratyahaara('हल्') and s[ii+1] not in avasaana:
            s = remove_avasaana(s)
    row = {'स्थिति': get_shabda(s), 'सूत्र': '-', 'टिप्पणी': '-'}
    df = df.append(row, ignore_index=True)

    return df

def word_seprator(s):

    ss =  s.split(' ')

    for ii in range(len(ss)):
        if get_vinyaasa(ss[ii])[-1] == 'ः':
            vv = get_vinyaasa(ss[ii])
            vv[-1] = 'स्'
            ss[ii] = get_shabda(vv)

    return ss

if __name__ == '__main__':

    query = yaml.safe_load(Path('input.yml').read_text())

    ww = word_seprator(query['वाक्य'])

    print(ww)

    df = None

    for ii in range(len(ww)):

        # print(ii)

        if ii == 0 or ww[ii-1] in avasaana:
            jj = ww[ii]
        else:
            jj = jj + ' ' + ww[ii]
            df = pada_sandhi(jj, df)
            jj = get_sthiti(df)
            # print(df)
            # print(jj)
            if ' ' in jj:
                qq = jj.split(' ')
                jj = qq[-1]
                print(qq[0], end=' ')
                if qq[-1] in avasaana:
                    print(qq[-1], end=' ')
        

    df.to_csv('output.csv', index=False)
