import pandas as pd
from varna import *
from vinyaasa import *
import pandas as pd
from pratyaahaara import *
from recorder import *

class Dhaatu:

    def __init__(self, ll):

        self.gana(ll)
        self.उपदेश = ll.split(' ')[1]

        fname = 'धातु/{}.md'.format(self.उपदेश)
        ff = start_recording(fname)
        record(ff, self.उपदेश, '-', '-')

        self.अर्थ = ' '.join(ll.split(' ')[2:-1])
        self.इत् = []
        self.पद = 'परस्मैपदी'
        self.इडागम = 'सेट्'

        self.it_lopa(ff)

        if len(self.इत्) > 0:
            record(ff, self.धातु, 'तस्य लोपः', 'इत्संज्ञकस्य लोपः')
        else:
            record(ff, self.धातु, 'शेषात् कर्तरि परस्मैपदम्', 'इति परस्मैपदम्')

        self.idaagama(ff)

        self.praakritika(ff)

        end_recording(ff)

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

    def it_lopa(self, ff):

        vv = get_vinyaasa(self.उपदेश)

        if vv[-1] in vyanjana and vv[-1] != 'र्':
            self.इत्.append(vv[-1])
            record(ff, vv, 'हलन्त्यम्', '{}-इत्यस्य इत्संज्ञा'.format(vv[-1]))
            if vv[-1] == 'ञ्':
                self.पद = "उभयपदी"
                record(ff, vv, 'स्वरितञितः कर्त्रभिप्राये क्रियाफले', 'इति उभयपदम्')
            if vv[-1] == 'ङ्':
                self.पद = "आत्मनेपदी"
                record(ff, vv, 'अनुदात्तङित आत्मनेपदम्', 'इति आत्मनेपदम्')
            del vv[-1]

        if get_shabda(vv[:2]) in ['ञि', 'टु', 'डु']:
            record(ff, vv, 'आदिर्ञिटुडवः', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[:2])))
            self.इत्.append(get_shabda(vv[:2]))
            del vv[:2]
        
        ii = 0

        while ii < len(vv):
            if vv[ii] in anunaasika_svara:

                if vv[ii] == 'इँ':
                    if (len(vv) == ii+2 and vv[ii+1] == 'र्') or (len(vv) == ii+3 and vv[ii+2] == 'र्'):
                        self.इत्.append('इर्')
                        record(ff, vv, 'इँर इत्संज्ञा वाच्या (वा)', '{}-इत्यस्य इत्संज्ञा'.format('इर्'))
                        del vv[ii]
                        del vv[-1]
    
                    else:
                        self.इत्.append('इ')
                        record(ff, vv, 'उपदेशेऽजनुनासिक इत्', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[ii])))
                        del vv[ii]

                else:
                    self.इत्.append(anunaasika_svara_to_svara[vv[ii]])
                    record(ff, vv, 'उपदेशेऽजनुनासिक इत्', '{}-इत्यस्य इत्संज्ञा'.format(get_shabda(vv[ii])))
                    del vv[ii]

                if ii >= len(vv):
                    self.पद = 'परस्मैपदी'
                    record(ff, self.उपदेश, 'शेषात् कर्तरि परस्मैपदम्', 'इति परस्मैपदम्')
                elif vv[ii] == '॒':
                    self.पद = 'आत्मनेपदी'
                    record(ff, self.उपदेश, 'अनुदात्तङित आत्मनेपदम्', 'इति आत्मनेपदम्')
                    del vv[ii]
                elif vv[ii] == '॑':
                    self.पद = 'उभयपदी'
                    record(ff, self.उपदेश, 'स्वरितञितः कर्त्रभिप्राये क्रियाफले', 'इति उभयपदम्')
                    del vv[ii]
                else:
                    self.पद = 'परस्मैपदी'
                    record(ff, vv, 'शेषात् कर्तरि परस्मैपदम्', 'इति परस्मैपदम्')

            

            ii += 1
        
        self.धातु = get_shabda(vv)

    def idaagama(self, ff):

        vv = get_vinyaasa(self.धातु)

        if '॒' in vv:
            self.इडागम = 'अनिट्'
            del vv[vv.index('॒')]
            record(ff, vv, '-', 'स्वरभेदमात्रालोपः')
        
        if 'ऊ' in self.इत्:
            self.इडागम = 'वेट्'

        self.धातु = get_shabda(vv)

    def praakritika(self, ff):

        vv = get_vinyaasa(self.धातु)

        if vv[0] == 'ष्':
            vv[0] = 'स्'

            if vv[1] == 'ट्':
                vv[1] = 'त्'
            elif vv[1] == 'ठ्':
                vv[1] = 'थ्'

            if 'ण्' in vv:

                jj = vv.index('ण्') - 1
                flag = True

                while jj > 0:
                    if vv[jj] in expand_pratyahaara('अट्') or s[ii] in ['क्', 'ख्', 'ग्', 'घ्', 'ङ्', 'प्', 'फ्', 'ब्', 'भ्', 'म्']:
                        pass
                    else:
                        f = False
                        break

                if flag:
                    vv[vv.index('ण्')] = 'न्'

            record(ff, vv, 'धात्वादेः षः सः', 'धातोरादेः षस्य सः')

        elif vv[0] == 'ण्':

            vv[0] == 'न्'

            record(ff, vv, 'णो नः', 'धातोरादेः णस्य नः')

        if 'इ' in self.इत्:

            jj = len(vv) - 1

            while jj >= 0:
                if vv[jj] in svara:
                    break
                jj -= 1
            
            vv.insert(jj+1, 'न्')
            record(ff, vv, 'इदितो नुम् धातोः', 'नुमागामः')

            if vv[jj+2] in expand_pratyahaara('झल्'):
                vv[jj+1] = 'ं'
                record(ff, vv, 'नश्चापदान्तस्य झलि', 'अनुस्वारः')

            if vv[jj+2] in expand_pratyahaara('यय्'):
                if vv[jj+2] in ['क्', 'ख्', 'ग्', 'घ्', 'ङ्']:
                    vv[jj+1] = 'ङ्'
                if vv[jj+2] in ['च्', 'छ्', 'ज्', 'झ्', 'ञ्']:
                    vv[jj+1] = 'ञ्'
                if vv[jj+2] in ['ट्', 'ठ्', 'ड्', 'ढ्', 'ण्']:
                    vv[jj+1] = 'ण्'
                if vv[jj+2] in ['त्', 'थ्', 'द्', 'ध्', 'न्']:
                    vv[jj+1] = 'न्'
                if vv[jj+2] in ['प्', 'फ्', 'ब्', 'भ्', 'म्']:
                    vv[jj+1] = 'म्'

                record(ff, vv, 'अनुस्वारस्य ययि परसवर्णः', 'परसवर्णः')

            if vv[jj+2] == 'ण्':
                vv[jj+1] = 'ण्'
                record(ff, vv, 'ष्टुना ष्टुः', 'ष्टुत्त्वम्')

        self.धातु = get_shabda(vv)


if __name__ == '__main__':

    with open('धातुपाठ_मूल.txt', 'r') as ff:
        s = ff.read()

    s = s.split('\n')

    d = [Dhaatu(w).__dict__ for w in s]

    df = pd.DataFrame(d)
    df = df.set_index('क्रमाङ्क')

    print(df)

    df.to_csv('धातु.csv')