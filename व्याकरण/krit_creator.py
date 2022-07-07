import pandas as pd
from varna import *
from vinyaasa import *
import pandas as pd
from pratyaahaara import *
from recorder import *

class Krit:

    def __init__(self, ll):

        self.उपदेश = ll
        self.इत् = []
        self.उच्चारण = -1
        
        self.find_uchchaarana()

        fname = 'कृत्/{}.md'.format(self.उपदेश)
        ff = start_recording(fname)
        record(ff, self.उपदेश, '-', '-')

        self.it_lopa(ff)

        if len(self.इत्) > 0:
            record(ff, self.प्रत्यय, 'तस्य लोपः', 'इत्संज्ञकस्य लोपः')

        if self.उच्चारण >= 0:
            self.remove_uchchaarana()
            record(ff, self.प्रत्यय, '-', 'उच्चारणार्थकवर्णस्य लोप')

        del self.उच्चारण

        self.get_prakaar(ff)

        end_recording(ff)

    def __repr__(self):
        return 'उपदेश   :   {} \nइत्   :   {} \nप्रत्यय   :   {}\nप्रकार   :   {}'.format(self.उपदेश, self.इत्, self.प्रत्यय, self.प्रकार)

    def get_prakaar(self,ff):
        
        if 'श्' in self.इत्:
            self.प्रकार = 'सार्वधातुक'
            record(ff, self.प्रत्यय, 'तिङ्शित्सार्वधातुकम्', 'शित्त्वात् कृत् सार्वधातुकम्')
        else:
            self.प्रकार = 'आर्धधातुक'
            record(ff, self.प्रत्यय, 'आर्धधातुकं शेषः', 'अशित्त्वात् कृत् आर्धधातुकम्')

    def find_uchchaarana(self):

        vv = get_vinyaasa(self.उपदेश)

        if '॒' in vv:
            self.उच्चारण = vv.index('॒') - 1
            del vv[self.उच्चारण + 1]

        self.उपदेश = get_shabda(vv)

    def remove_uchchaarana(self):
        
        vv = get_vinyaasa(self.प्रत्यय)
        del vv[self.उच्चारण]
        self.प्रत्यय = get_shabda(vv)

    def it_lopa(self, ff):

        vv = get_vinyaasa(self.उपदेश)

        if vv[0] in ['च्', 'छ्', 'ज्', 'झ्', 'ञ्', 'ट्', 'ठ्', 'ड्', 'ढ्', 'ण्']:
            self.इत्.append(vv[0])
            record(ff, self.उपदेश, 'चुटू', '{}-इत्यस्य इत्संज्ञा'.format(vv[0]))
            del vv[0]
            self.उच्चारण -= 1
        elif vv[0] in ['ल्', 'श्', 'क्', 'ख्', 'ग्', 'घ्', 'ङ्']:
            self.इत्.append(vv[0])
            record(ff, self.उपदेश, 'लशक्वतद्धिते', '{}-इत्यस्य इत्संज्ञा'.format(vv[0]))
            del vv[0]
            self.उच्चारण -= 1
        
        if vv[-1] in vyanjana:
            self.इत्.append(vv[-1])
            record(ff, self.उपदेश, 'हलन्त्यम्', '{}-इत्यस्य इत्संज्ञा'.format(vv[-1]))
            del vv[-1]

        self.प्रत्यय = get_shabda(vv)

if __name__ == '__main__':

    with open('कृत्.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')

    # d = s[83]
    # print(d)

    d = [Krit(w).__dict__ for w in s]

    df = pd.DataFrame(d)

    print(df)

    df.to_csv('कृत्.csv')

    # xx = Krit(d)

    # print(xx)