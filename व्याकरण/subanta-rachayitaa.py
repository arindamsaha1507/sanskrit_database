from pratyaahaara import expand_pratyahaara
from sutra import *
# from vaakya_sandhi import vaakya_sandhi
from vinyaasa import get_shabda, get_vinyaasa


def give_samjya(w, tag, force=None):

    sarvanaama = 'सर्व विश्व उभ उभय कतर कतम यतर यतम ततर ततम एकतर एकतम इतर त्वत् त्व नेम सम सिम पूर्व पर अवर दक्षिण उत्तर अपर अधर स्व अन्तर त्यद् तद् यद् एतद् इदम् अदस् एक द्वि युष्मद् अस्मद् भवतुँ किम्'
    sarvanaama = sarvanaama.split(' ')

    if force != None:
        tag.append(force)
    else:
        if w in sarvanaama:
            tag.append('सर्वनाम')

    return tag

def subaadesha(df, pr, it, tag, word, vibhakti, vachana, linga):

    if vibhakti == 8 and vachana == 1:
        give_samjya(get_shabda(pre_processing(df)), tag, force='सम्बुद्धि')

    if get_vinyaasa(word)[-1] == 'अ':

        if 'सर्वनाम' in tag:

            if pr == 'ङे':
                df, pr, it = सर्वनाम्नः_स्मै(df, pr, tag)
            if pr in ['ङसिँ', 'ङि']:
                df, pr, it = ङसिङ्योः_स्मात्स्मिनौ(df, pr, tag)
            if pr == 'जस्':
                df, pr, it = जसः_शी(df, pr, tag)

        if pr == 'भिस्':
            df, pr, it = अतो_भिस_ऐस्(df, pr)
        if pr in ['टा', 'ङसिँ', 'ङस्']:
            df, pr, it = टाङसिङसामिनात्स्याः(df, pr)
        if pr == 'ङे':
            df, pr, it = ङेर्यः(df, pr)

    if get_vinyaasa(word)[-1] in ['अ', 'आ'] and 'सर्वनाम' in tag:

        if pr == 'आम्':
            df, pr, it = आमि_सर्वनाम्नः_सुट्(df, pr, tag)

    if get_vinyaasa(word)[-1] in ['अ', 'इ', 'उ', 'ऋ', 'ऌ'] or 'नदी' in tag:

        if pr == 'आम्':
            df, pr, it = ह्रस्वनद्यापो_नुट्(df, pr, tag)

    if 'सम्बुद्धि' in tag:

        s = pre_processing(df)

        s = get_shabda(s)
        s = s.split(' ')

        if get_vinyaasa(s[0])[-1] in ['अ', 'इ', 'उ', 'ऋ', 'ऌ'] or get_vinyaasa(s[0])[-1] in expand_pratyahaara('एङ्'):
            df, pr, it = एङ्ह्रस्वात्_सम्बुद्धेः(df, pr, tag)

    return df, pr, it, tag

def angaadesha(df, pr, it, tag, word, vibhakti, vachana, linga):

    s = pre_processing(df)

    anga = s[:s.index(' ')]
    pr = s[s.index(' ')+1:]

    if anga[-1] == 'अ' and get_shabda(pr) == 'ओस्' and 'सुप्' in tag:
        df = ओसि_च(df, pr, tag)

    if anga[-1] == 'अ' and pr[0] in expand_pratyahaara('झल्') and vachana == 3 and 'सुप्' in tag:
        df = बहुवचने_झल्येत्(df, pr, tag)

    if anga[-1] == 'अ' and pr[0] in expand_pratyahaara('यञ्') and 'सुप्' in tag:
        df = सुपि_च(df, pr, tag)

    return df, pr, it, tag

def sandhi(df, pr, it, tag, word, vibhakti, vachana, linga):

    s = pre_processing(df)
    ii = s.index(' ')

    if s[ii-1] in expand_pratyahaara('अक्') and s[ii+1] in expand_pratyahaara('अच्'):
        if pr == 'अम्':
            df = अमि_पूर्वः(df, pr)
        elif vibhakti in [1,2,8]:
            if (s[ii-1] == 'अ' and s[ii+1] in ['अ', 'आ']) or (s[ii-1] in ['आ', 'ई', 'ऊ'] and s[ii+1] in ['अ', 'आ'] and pr != 'जस्') or (s[ii-1] in ['इ', 'उ', 'ऋ']):
                df = प्रथमयोः_पूर्वसवर्णः(df, vibhakti, vachana, linga)
    
    s = pre_processing(df)
    if ' ' in s:
        ii = s.index(' ')

        if (s[ii-1] == s[ii+1] and s[ii-1] in expand_pratyahaara('अक्')) or (set((s[ii-1], s[ii+1])) in [set(('अ', 'आ')), set(('इ', 'ई')), set(('उ', 'ऊ')), set(('ऋ', 'ॠ')), set(('ऋ', 'ऌ')), set(('ॠ', 'ऌ'))]):
            df = अकः_सवर्णे_दीर्घः(df)
        elif s[ii-1] in ['अ', 'आ'] and s[ii+1] in expand_pratyahaara('एच्'):
            df = वृद्धिरेचि(df)
        elif s[ii-1] in ['अ', 'आ'] and s[ii+1] in expand_pratyahaara('अक्'):
            df = आद्गुणः(df)
        elif s[ii-1] in expand_pratyahaara('एच्') and s[ii+1] in expand_pratyahaara('अच्'):
            df = एचोऽयवायावः(df, pada=False)
        elif s[ii-1] in expand_pratyahaara('इक्') and s[ii+1] in expand_pratyahaara('अच्'):
            df = इको_यणचि(df)

    s = pre_processing(df)
    if ' ' in s:
        ii = s.index(' ')
        del s[ii]
        row = {'स्थिति': get_shabda(s), 'सूत्र': '-'}
        df = df.append(row, ignore_index=True)

    return df

if __name__ == '__main__':

    df = pd.DataFrame(columns=['स्थिति', 'सूत्र'])

    word = 'नर'
    linga = 1

    vibhakti = 6
    vachana = 3

    tag = give_samjya(word, [])

    row = {'स्थिति': word, 'सूत्र': '-'}
    df = df.append(row, ignore_index=True)

    df, pr, it = स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाङ्ङ्योस्सुप्(df, vibhakti, vachana)
    tag = give_samjya(word, tag, force='सुप्')

    df, pr, it, tag = subaadesha(df, pr, it, tag, word, vibhakti, vachana, linga)
    df, pr, it, tag = angaadesha(df, pr, it, tag, word, vibhakti, vachana, linga)

    s = pre_processing(df)

    if get_shabda(pr) == 'सु':
        df = आदेशप्रत्यययोः(df, len(s)-2)

    if 'न्' in s and ('र्' in s or 'ष्' in s):
        df = अट्कुप्वाङ्नुम्व्यवायेऽपि(df)

    df = sandhi(df, pr, it, tag, word, vibhakti, vachana, linga)


    print(df)
