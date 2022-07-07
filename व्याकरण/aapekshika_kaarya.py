from get_dhaatu import get_dhaatu
from get_krit import get_krit
from recorder import *
from vinyaasa import *
from pratyaahaara import *

def find_dhaatu(dd):

    d = get_dhaatu(dd)

    if len(d) == 1:
        print('{}स्य {}-धातुः प्राप्तः'.format(d[0].गण, d[0].धातु))
        return d[0]
    elif len(d) == 0:
        print('धातुः न प्राप्तः')
    else:
        print('नैकाः धातवः प्राप्ताः')

def get_sthiti(up, dh, pr):
    if up == None:
        sthiti = '{} {}'.format(dh.धातु, pr.प्रत्यय)
    else:
        sthiti = '{} {} {}'.format(up.पद, dh.धातु, pr.प्रत्यय)
    
    return sthiti

def pratyaya_aadesh(ff, up, dh, pr):

    if pr.प्रत्यय == 'यु':
        pr.प्रत्यय = 'अन'
        record(ff, get_sthiti(up, dh, pr), 'युवोरनाकौ', 'अङ्गात् यु-इत्यस्य अन-आदेशः')
    elif pr.प्रत्यय == 'वु':
        pr.प्रत्यय = 'अक'
        record(ff, get_sthiti(up, dh, pr), 'युवोरनाकौ', 'अङ्गात् वु-इत्यस्य अक-आदेशः')
    elif pr.प्रत्यय == 'व्':
        pr.प्रत्यय = '०'
        record(ff, get_sthiti(up, dh, pr), 'वेरपृक्तस्य', 'अङ्गात् अपृक्तस्य वकारस्य लोपः')
    elif pr.उपदेश == 'क्त्वा' and up != None and up.उपदेश != 'नञ्':
        pr.प्रत्यय = 'ल्यप्'
        record(ff, get_sthiti(up, dh, pr), 'समासेऽनञ्पूर्वे क्त्वो ल्यप्', 'अव्ययपूर्वपदे अनञ्समासे क्त्वो ल्यप्')
        record(ff, get_sthiti(up, dh, pr), 'लशक्वतद्धिते', 'ल्-इत्यस्य इत्संज्ञा')
        record(ff, get_sthiti(up, dh, pr), 'हलन्त्यम्', 'प्-इत्यस्य इत्संज्ञा')

        pr.प्रत्यय = 'य'
        pr.इत्.append('ल्')
        pr.इत्.append('प्')
        record(ff, get_sthiti(up, dh, pr), 'तस्य लोपः', 'इत्संज्ञकस्य लोपः')

def dhaatu_kaarya(ff, up, dh, pr):

    if pr.प्रकार == 'आर्धधातुक':
        
        if dh.धातु == 'अद्':
            if 'क्' in pr.इत्:
                dh.धातु = 'जग्ध्'
                record(ff, get_sthiti(up, dh, pr), 'अदो जग्धिर्ल्यप्ति किति', 'आर्धधातुके किति परे अद-धातोः जग्ध्-आदेशः')
            elif pr.उपदेश == 'घञ्' or pr.उपदेश == 'अप्':
                dh.धातु = 'घस्'
                record(ff, get_sthiti(up, dh, pr), 'घञपोश्च', 'घञ्-परे अप्-परे च अद-धातोः घस्-आदेशः')
        elif dh.धातु == 'अस्':
            dh.धातु = 'भू'
            record(ff, get_sthiti(up, dh, pr), 'अस्तेर्भूः', 'आर्धधातुके परे अस्-धातोः भू-आदेशः')
        elif dh.धातु == 'ब्रू':
            dh.धातु = 'वच्'
            record(ff, get_sthiti(up, dh, pr), 'ब्रुवो वचिः', 'आर्धधातुके परे ब्रू-धातोः वच्-आदेशः')
        elif dh.धातु == 'चक्ष्':
            dh.धातु = 'ख्या'
            record(ff, get_sthiti(up, dh, pr), 'चक्षिङः ख्याञ्', 'आर्धधातुके परे चक्ष्-धातोः ख्या-आदेशः')
        elif dh.धातु == 'अज्' and pr.उपदेश not in ['घञ्', 'अप्', 'क्यप्']:
            dh.धातु = 'वी'
            record(ff, get_sthiti(up, dh, pr), 'अजेर्व्यघञपोः', 'आर्धधातुके परे अज्-धातोः वी-आदेशः')
        elif get_vinyaasa(dh.धातु)[-1] in expand_pratyahaara('एच्'):
            vv = get_vinyaasa(dh.धातु)
            vv[-1] = 'आ'
            dh.धातु = get_shabda(vv)
            record(ff, get_sthiti(up, dh, pr), 'आदेच उपदेशेऽशिति', 'एजान्तस्य धातोः आ-आदेशः अशिति')
        elif dh.उपदेश in ['मी॒ञ्', 'डुमि॒ञ्', 'दीङ्', 'ली॒', 'ली॒ङ्'] and (('क्' not in pr.इत् and 'ङ्' not in pr.इत्) or (up != None and pr.उपदेश == क्त्वा)):
            vv = get_vinyaasa(dh.धातु)
            vv[-1] = 'आ'
            dh.धातु = get_shabda(vv)
            record(ff, get_sthiti(up, dh, pr), 'मीनातिमिनोतिदीङां ल्यपि च', 'आ-आदेशः अशिति')

def test_idaagama(ff, up, dh, pr, option=0):

    if pr.प्रकार == 'आर्धधातुक':

        if get_vinyaasa(pr.प्रत्यय)[0] in expand_pratyahaara('वल्'):
            
            if get_vinyaasa(pr.प्रत्यय)[0] in expand_pratyahaara('वश्'):
                record(ff, get_sthiti(up, dh, pr), 'नेड् वशि कृति', 'वशादि आर्धधातुक-कृत्-प्रत्ययः इडागमं नैव स्वीकरोति')
                return False
            else:

                if pr.उपदेश in ['क्तिच्', 'क्तिन्', 'ष्ट्रन्']:
                    record(ff, get_sthiti(up, dh, pr), 'तितुत्रतथसिसुसरकसेषु च', 'क्तिच्, क्तिन्, ष्ट्रन् - एतेषां इट् न')
                    return False

    else:

        record(ff, get_sthiti(up, dh, pr), '-', 'सार्वधातुके इट् न')
        return False

    
    if dh.इडागम == 'अनिट्':

        record(ff, get_sthiti(up, dh, pr), '-', 'अनिट्-धातोः इट् न')
        return False

    if get_vinyaasa(dh.धातु)[-1] == 'उ' and pr.उपदेश in ['क्त्वा','क्त', 'क्तवतु']:
        record(ff, get_sthiti(up, dh, pr), 'श्र्युकः क्किति', 'उगन्ताचः परयोः कितोः इट् न स्यात्')
        return False

    if 'उ' in dh.इत् and pr.उपदेश in ['क्त', 'क्तवतु']:
        record(ff, get_sthiti(up, dh, pr), 'यस्य विभाषा', 'क्त्वाप्रत्ययस्य इड्विकल्पे प्राप्ते निष्ठा-प्रत्यययोः इट् न')
        return False

    if 'उ' in dh.इत् and pr.उपदेश == 'क्त्वा':
        record(ff, get_sthiti(up, dh, pr), 'उदितो वा', 'उदितः परस्य क्त्वाप्रत्ययस्य इड्विकल्पः')
        if option == 0:
            return False
        else:
            return True

    if 'ई' in dh.इत् and pr.उपदेश in ['क्त', 'क्तवतु']:
        record(ff, get_sthiti(up, dh, pr), 'श्वीदितो निष्ठायाम्', 'ईदितः परस्य निष्ठा-प्रत्यययोः इट् न')
        return False

    if 'आ' in dh.इत् and pr.उपदेश in ['क्त', 'क्तवतु']:
        if option == 0:
            record(ff, get_sthiti(up, dh, pr), 'आदितश्च', 'आकारेतोः निष्ठायाः इट् न')
            return False
        else:
            record(ff, get_sthiti(up, dh, pr), 'विभाषा भावादिकर्मणोः', 'भावे आदिकर्मणि चादितो निष्ठाया इड्वा')

    if dh.इडागम == 'सेट्':
        return True
    
    if option == 0:
        return False
    else:
        return True

def apply_idaagama(ff, up, dh, pr):

    vv = get_vinyaasa(pr.प्रत्यय)
    vv.insert(0, 'इट्-')
    pr.प्रत्यय = get_shabda(vv)
    record(ff, get_sthiti(up, dh, pr), 'आर्धधातुकस्येड् वलादेः', 'वलादि आर्धधातुकप्रत्ययः इडागमः')
    record(ff, get_sthiti(up, dh, pr), 'हलन्त्यम्', 'ट्-इत्यस्य इत्संज्ञा, टित्त्वात् आद्यागमः')

    vv = get_vinyaasa(pr.प्रत्यय)
    del vv[1]
    pr.प्रत्यय = get_shabda(vv)
    record(ff, get_sthiti(up, dh, pr), 'तस्य लोपः', 'इत्संज्ञकस्य लोपः')

    vv = get_vinyaasa(pr.प्रत्यय)
    del vv[1]
    pr.प्रत्यय = get_shabda(vv)
    record(ff, get_sthiti(up, dh, pr), '-', 'वर्णमेलनम्')

if __name__ == '__main__':

    fname = 'test.md'

    up = None

    ff = start_recording(fname)

    dd = {
        'धातु': 'कृ',
        'गण': 'तनादि'
    }

    dh = find_dhaatu(dd)
    if dh == None:
        exit()

    
    pr = get_krit('तुमुन्')

    record(ff, get_sthiti(up, dh, pr), '-', '-')

    dhaatu_kaarya(ff, up, dh, pr)
    pratyaya_aadesh(ff, up, dh, pr)
    if test_idaagama(ff, up, dh, pr):
        apply_idaagama(ff, up, dh, pr)


    end_recording(ff)