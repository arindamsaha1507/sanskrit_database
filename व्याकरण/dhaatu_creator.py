import pandas as pd
from varna import *
from vinyaasa import *
import pandas as pd
from pratyaahaara import *
from recorder import *
from sutra import *

class Dhaatu:

    def __init__(self, ll, df=None):

        self.gana(ll)
        self.उपदेश = ll.split(' ')[1]

        fname = 'धातु/{}.csv'.format(self.उपदेश)

        if df is None:
            df = pd.DataFrame(columns=['स्थिति', 'सूत्र', 'टिप्पणी'])
        
        row = {'स्थिति': self.उपदेश, 'सूत्र': '-', 'टिप्पणी': '-'}
        df = df.append(row, ignore_index=True)

        self.अर्थ = ' '.join(ll.split(' ')[2:-1])
        self.इत् = []

        df, anudaatta, svarita = self.it_lopa(df)
        df = self.pada_nirnaya(df, anudaatta, svarita)
        df = self.idaagama(df)
        df = self.praakritika(df)

        df.to_csv(fname, index=False)

    def __repr__(self):

        return 'धातु : {} \nअर्थ : {} \nगण : {} \nपद : {}\nइडागम : {} \nउपदेश : {} \nइत् : {}'.format(self.धातु, self.अर्थ, self.गण, self.पद, self.इडागम, self.उपदेश, ' '.join(self.इत्))

    def gana(self, ll):

        d = {
            '१': 'भ्वादि',
            '२': 'अदादि',
            '३': 'जुहोत्यादि',
            '४': 'दिवादि',
            '५': 'स्वादि',
            '६': 'तुदादि',
            '७': 'रुधादि',
            '८': 'तनादि',
            '९': 'क्र्यादि',
            '१०': 'चुरादि'
        }

        self.क्रमाङ्क = ll.split(' ')[0]
        self.गण = d[self.क्रमाङ्क.split('.')[0]]

    def it_lopa(self, df):

        vv = get_vinyaasa(self.उपदेश)

        svarita = []
        anudaatta = []
        anunaasika = []

        for ii in range(len(vv)):
            if vv[ii] == '॑':
                svarita.append(ii-1)
            if vv[ii] == '॒':
                anudaatta.append(ii-1)
            if vv[ii] in anunaasika_svara:
                anunaasika.append(ii)


        if len(anunaasika) > 0:
            df, aa = उपदेशेऽजनुनासिक_इत्(df, anunaasika)
            self.इत्.extend(aa)
        
        if vv[-1] in expand_pratyahaara('हल्'):
            df, bb = हलन्त्यम्(df)
            self.इत्.append(bb)

        if get_shabda(vv[:2]) in ['ञि', 'टु', 'डु']:
            df, cc = आदिर्ञिटुडवः(df)
            self.इत्.append(cc)

        if len(self.इत्) > 0:
            df = तस्य_लोपः(df,ii='dhaatu')

        return df, anudaatta, svarita

    def pada_nirnaya(self, df, anudaatta, svarita):

        if len(self.इत्) == 0:
            df = शेषात्_कर्तरि_परस्मैपदम्(df)
            self.पद = 'परस्मैपदी'
        else:
            if 'ञ्' in self.इत् or len(svarita) > 0:
                df = स्वरितञितः_कर्त्रभिप्राये_क्रियाफले(df)
                self.पद = 'उभयपदी'
            elif 'ङ्' in self.इत् or len(anudaatta) > 0:
                df = अनुदात्तङित_आत्मनेपदम्(df)
                self.पद = 'आत्मनेपदी'
            else:
                df = शेषात्_कर्तरि_परस्मैपदम्(df)
                self.पद = 'परस्मैपदी'

        self.धातु = get_shabda(get_sthiti(df))
        return df

        # print(df)
        # print(self.इत्)

        # if vv[-1] in vyanjana and vv[-1] != 'र्':
        #     self.इत्.append(vv[-1])
        #     record(ff, vv, 'हलन्त्यम्', '{}-इत्यस्य इत्संज्ञा'.format(vv[-1]))
        #     if vv[-1] == 'ञ्':
        #         self.पद = "उभयपदी"
        #         record(ff, vv, 'स्वरितञितः कर्त्रभिप्राये क्रियाफले', 'इति उभयपदम्')
        #     if vv[-1] == 'ङ्':
        #         self.पद = "आत्मनेपदी"
        #         record(ff, vv, 'अनुदात्तङित आत्मनेपदम्', 'इति आत्मनेपदम्')
        #     del vv[-1]

        # if get_shabda(vv[:2]) in ['ञि', 'टु', 'डु']:
        #     record(ff, vv, 'आदिर्ञिटुडवः', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[:2])))
        #     self.इत्.append(get_shabda(vv[:2]))
        #     del vv[:2]
        
        # ii = 0

        # while ii < len(vv):
        #     if vv[ii] in anunaasika_svara:

        #         if vv[ii] == 'इँ':
        #             if (len(vv) == ii+2 and vv[ii+1] == 'र्') or (len(vv) == ii+3 and vv[ii+2] == 'र्'):
        #                 self.इत्.append('इर्')
        #                 record(ff, vv, 'इँर इत्संज्ञा वाच्या (वा)', '{}-इत्यस्य इत्संज्ञा'.format('इर्'))
        #                 del vv[ii]
        #                 del vv[-1]
    
        #             else:
        #                 self.इत्.append('इ')
        #                 record(ff, vv, 'उपदेशेऽजनुनासिक इत्', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[ii])))
        #                 del vv[ii]

        #         else:
        #             self.इत्.append(anunaasika_svara_to_svara[vv[ii]])
        #             record(ff, vv, 'उपदेशेऽजनुनासिक इत्', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[ii])))
        #             del vv[ii]

        #         if ii >= len(vv):
        #             self.पद = 'परस्मैपदी'
        #             record(ff, self.उपदेश, 'शेषात् कर्तरि परस्मैपदम्', 'इति परस्मैपदम्')
        #         elif vv[ii] == '॒':
        #             self.पद = 'आत्मनेपदी'
        #             record(ff, self.उपदेश, 'अनुदात्तङित आत्मनेपदम्', 'इति आत्मनेपदम्')
        #             del vv[ii]
        #         elif vv[ii] == '॑':
        #             self.पद = 'उभयपदी'
        #             record(ff, self.उपदेश, 'स्वरितञितः कर्त्रभिप्राये क्रियाफले', 'इति उभयपदम्')
        #             del vv[ii]
        #         else:
        #             self.पद = 'परस्मैपदी'
        #             record(ff, vv, 'शेषात् कर्तरि परस्मैपदम्', 'इति परस्मैपदम्')

            

            # ii += 1
        
        self.धातु = get_shabda(vv)

    def idaagama(self, df):

        vv = get_vinyaasa(self.धातु)

        cc = len([x for x in vv if x in svara])

        if '॒' in vv and cc == 1:
            df = एकाच_उपदेशेऽनुदात्तात्(df)
            self.इडागम = 'अनिट्'
            self.धातु = get_shabda(get_sthiti(df))
        
        elif 'ऊ' in self.इत्:
            df = स्वरतिसूतिसूयतिधूञूदितो_वा(df)
            self.इडागम = 'वेट्'

        else:
            self.इडागम = 'सेट्'

        return df

    def praakritika(self, df):

        vv = get_vinyaasa(self.धातु)

        if vv[0] == 'ष्':
            df = धात्वादेः_षः_सः(df)
        elif vv[0] == 'ण्':
            df = णो_नः(df)

        if 'इ' in self.इत्:

            df, jj = इदितो_नुम्_धातोः(df)

            vv = get_vinyaasa(get_sthiti(df))

            print(vv, jj)

            if vv[jj+2] in expand_pratyahaara('झल्'):

                df = नश्चापदान्तस्य_झलि(df, jj+1)
                df = अनुस्वारस्य_ययि_परसवर्णः(df, jj+1)

        self.धातु = get_shabda(get_sthiti(df))
        
        return df


if __name__ == '__main__':

    # dd = Dhaatu('१.१८ ष्वदँ॒ आ॒स्वाद॑ने ।')

    # print(dd)

    with open('धातुपाठ_मूल.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')

    d = [Dhaatu(w).__dict__ for w in s]

    df = pd.DataFrame(d)
    df = df.set_index('क्रमाङ्क')

    print(df)

    df.to_csv('धातु_1.csv')