import random
import re

SPACEFREQUENCY = 1.2
quotechar = '"'


def tococanb(sentence):
    punc = list()
    for i in range(len(sentence)):
        if sentence[i] == '.' or sentence[i] == '!' or sentence[i] == '?':
            punc.append(sentence[i])
    if sentence[-1] != '.' or sentence[-1] != '?' or sentence[-1] != '!':
        punc.append('.')
    sentence = sentence.replace('.', '▞').replace('?', '▞').replace('!', '▞')
    sentencelist = sentence.split('▞')
    if '' in sentencelist:
        sentencelist.remove('')
    for i in range(len(sentencelist)):
        sentencelist[i] = translate(sentencelist[i])
        sentencelist[i] = sentencelist[i][0].upper() + sentencelist[i][1:]
    sentence = '▞ '.join(sentencelist) + '▞'
    for i in range(sentence.count('▞')):
        sentence = sentence.replace('▞', punc[i], 1)
    return sentence


def addspaces(s, n):
    vowelsyll = ['a', 'e', 'i', 'o', 'u', 'y', 'ň', 'ř', 'ł']
    where = random.sample(range(2, len(s)), n)
    where.append(0)
    where.append(len(s))
    where.sort()
    where2 = where
    i = 1
    while i <= len(where):
        if (where2[i]) + 1 in where2:
            where2.remove((where2[i]) + 1)
        else:
            pass
        i += 1
        if i >= len(where):
            break
    where = where2
    if 0 in where:
        where.remove(0)
    if len(s) in where:
        where.remove(len(s))
    if len(s) - 1 in where:
        where.remove(len(s) - 1)
    if len(s) - 2 in where:
        where.remove(len(s) - 2)
    slist = list(s)
    for i in range(len(slist) - 1):
        if i in where:
            if any(v in vowelsyll for v in slist[i]):
                slist[i] = slist[i] + ' '
            else:
                slist[i] = slist[i]
    return ''.join(slist)


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n - 1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


def translate(sentence):
    sentence = sentence.replace(',', '').replace('-', '').replace("'", "")
    sentence = sentence.lower()
    sentence = sentence.replace('œ', 'oe').replace('æ', 'ae')
    sentencelist = sentence.split()
    finishlist = list()
    afternon = list()

    #before the separator non
    for i in range(len(sentencelist)):
        finishlist.append(sentencelist[i][:-1])

    #after the separator non
    for i in range(len(sentencelist)):
        if len(sentencelist[i]) <= 26:
            afternon.append(sentencelist[i][-1] +
                            chr(len(sentencelist[i]) + 96))
        elif len(sentencelist[i]) > 26:
            afternon.append(sentencelist[i][-1] + 'å' +
                            chr(len(sentencelist[i]) + 96 - 26))

    #adding the separator non
    finishlist = ''.join(finishlist) + 'n'
    afternon = 'n' + ''.join(afternon)
    finishlist = finishlist.replace('non', 'nôn')
    afternon = afternon.replace('non', 'nôn')
    finishlist = finishlist.replace('non', 'nôn')
    afternon = afternon.replace('non', 'nôn')
    cocanb = finishlist[:-1] + '▟' + afternon[1:]

    #consonant and vowel lists
    consonant = [
        'q', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
        'c', 'v', 'b', 'n', 'm', 'h', ' '
    ]
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']

    cocanb = cocanb.replace('cocán', '■')
    cocanb = cocanb.replace('cocan', '■')

    #inserting syllabic diacritics (ň)
    for i in range(1, len(cocanb) - 1):
        if cocanb[i] == 'n':
            consonant.remove('n')
            if cocanb[i - 1] in consonant and cocanb[i + 1] in consonant:
                cocanb = cocanb[:i] + 'ň' + cocanb[i + 1:]
            consonant.append('n')

    for i in range(len(cocanb)):
        if cocanb[i] == 'n':
            cocanb = cocanb[:i] + random.choice(['n', 'n', 'ń'
                                                 ]) + cocanb[i + 1:]

    #inserting spaces
    if len(cocanb) > 10:
        cocanb = addspaces(cocanb, int((len(cocanb)) / SPACEFREQUENCY))
    elif len(cocanb) <= 10 and len(cocanb) > 4:
        cocanb = addspaces(cocanb, 2)
    else:
        cocanb = cocanb

    #inserting syllabic diacritics (ř and ł)
    for i in range(1, len(cocanb) - 1):
        if cocanb[i] == 'l':
            consonant.remove('l')
            if cocanb[i - 1] in consonant and cocanb[i + 1] in consonant:
                cocanb = cocanb[:i] + 'ł' + cocanb[i + 1:]
            consonant.append('l')

        if cocanb[i] == 'r':
            consonant.remove('r')
            if cocanb[i - 1] in consonant and cocanb[i + 1] in consonant:
                cocanb = cocanb[:i] + 'ř' + cocanb[i + 1:]
            consonant.append('r')

    #đ
    for i in range(1, len(cocanb)):
        if cocanb[i] == 'd':
            consonant.remove('d')
            if cocanb[i - 1] in ['t']:
                if i == len(cocanb):
                    cocanb = cocanb[:i] + 'đ'
                else:
                    cocanb = cocanb[:i] + 'd' + cocanb[i + 1:]
            consonant.append('d')

    #ğ
    if cocanb[-1] == 'g':
        cocanb = cocanb[:-1] + 'ğ'
    for i in range(1, len(cocanb) - 1):
        if cocanb[i] == 'g':
            if cocanb[i - 1] in vowel:
                cocanb = cocanb[:i] + 'ğ' + cocanb[i + 1:]
            if cocanb[i - 1] in consonant and cocanb[i + 1] in vowel:
                cocanb = cocanb[:i] + 'ğ' + cocanb[i + 1:]
            else:
                pass

    #æ digraph
    for i in range(cocanb.count('ae')):
        cocanb = cocanb.replace('ae', random.choice(['ae', 'ae', 'æ']), 1)

    #œ digraph
    for i in range(cocanb.count('oe')):
        cocanb = cocanb.replace('oe', random.choice(['oe', 'oe', 'œ']), 1)

    #vowel diacritics
    for i in range(len(cocanb)):
        if cocanb[i] == 'a':
            cocanb = cocanb[:i] + random.choice([
                'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'á', 'á', 'â', 'â',
                'à', 'à', 'ä'
            ]) + cocanb[i + 1:]
        if cocanb[i] == 'e':
            cocanb = cocanb[:i] + random.choice([
                'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'é', 'é', 'ê', 'ê',
                'è', 'è', 'ë'
            ]) + cocanb[i + 1:]
        if cocanb[i] == 'i':
            cocanb = cocanb[:i] + random.choice([
                'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'í', 'í', 'î', 'î',
                'ì', 'ì'
            ]) + cocanb[i + 1:]
        if cocanb[i] == 'o':
            cocanb = cocanb[:i] + random.choice([
                'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'ó', 'ó', 'ô', 'ô',
                'ò', 'ò', 'ö'
            ]) + cocanb[i + 1:]
        if cocanb[i] == 'u':
            cocanb = cocanb[:i] + random.choice([
                'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'ú', 'ú', 'û', 'û',
                'ù', 'ù', 'ü'
            ]) + cocanb[i + 1:]

    #sc, ść, šč
    for i in range(len(cocanb) - 1):
        if cocanb[i:i + 2] == 'sc':
            rand_sc = random.choice(['┃┃', 'ść', 'šč'])
            cocanb = cocanb[:i] + rand_sc + cocanb[i + 2:]

    #y and ý
    for i in range(1, len(cocanb) - 1):
        if cocanb[i] == 'y':
            if cocanb[i - 1] in consonant and cocanb[i + 1] in consonant:
                cocanb = cocanb[:i] + random.choice(['y', 'ý', 'ý'
                                                     ]) + cocanb[i + 1:]

    #c, s, z
    for i in range(len(cocanb)):
        if cocanb[i] == 'c':
            cocanb = cocanb[:i] + random.choice(['c', 'c', 'č', 'ć'
                                                 ]) + cocanb[i + 1:]
        if cocanb[i] == 's':
            cocanb = cocanb[:i] + random.choice(['s', 's', 'š', 'ś'
                                                 ]) + cocanb[i + 1:]
        if cocanb[i] == 'z':
            cocanb = cocanb[:i] + random.choice(['z', 'z', 'ž', 'ź'
                                                 ]) + cocanb[i + 1:]

    cocanb = cocanb.replace('■', 'Cocán')
    cocanb = cocanb.replace('▟', 'non')
    cocanb = cocanb.replace('┃┃', 'sc')
    return cocanb


def ctranslate(sentence):
    quotelistout = sentence.split('"')
    quotelist = list()
    for i in range(len(quotelistout)):
        if i % 2 == 1:
            quotelist.append(quotelistout[i])
        else:
            pass
    for i in range(len(quotelist)):
        sentence = sentence.replace(quotechar + quotelist[i] + quotechar, '▶▷',
                                    1)
    totalnumlist = re.findall(r'\d+', sentence)
    isolatenumlist = re.findall(r'\b\d+\b', sentence)
    endnumlist = re.findall(r'\d+\b', sentence)
    endnumlist = [x for x in endnumlist if x not in isolatenumlist]
    middlenumlist = [x for x in totalnumlist if x not in isolatenumlist]
    middlenumlist = [x for x in middlenumlist if x not in endnumlist]
    for i in range(len(isolatenumlist)):
        sentence = sentence.replace(isolatenumlist[i], '▲△', 1)
    for i in range(len(endnumlist)):
        sentence = sentence.replace(endnumlist[i], '▽', 1)
    for i in range(len(middlenumlist)):
        sentence = sentence.replace(middlenumlist[i], '◉', 1)

    print(totalnumlist)
    print(isolatenumlist)
    print(endnumlist)
    print(middlenumlist)
    for i in range(len(quotelist)):
        if '.' in quotelist[i] or '!' in quotelist[i] or '?' in quotelist[i]:
            quotelist[i] = tococanb(quotelist[i])
        else:
            quotelist[i] = translate(quotelist[i])
    sentence = tococanb(sentence)

    for i in range(sentence.count('▲')):
        sentence = sentence.replace('▲', ' ' + isolatenumlist[i] + ' ', 1)
    for i in range(sentence.count('▽')):
        sentence = sentence.replace('▽', endnumlist[i] + ' ', 1)
    for i in range(sentence.count('◉')):
        sentence = sentence.replace('◉', middlenumlist[i], 1)
    for i in range(len(sentence)):
        if sentence[i] == '△':
            sentence = sentence[:i] + '△△' + sentence[i + 2:]
    sentence = sentence.replace('△△', '')

    for i in range(sentence.count('▶')):
        sentence = sentence.replace(
            '▶', ' ' + quotechar + quotelist[i] + quotechar + ' ', 1)
    for i in range(len(sentence)):
        if sentence[i] == '▷':
            sentence = sentence[:i] + '▷▷' + sentence[i + 2:]
    sentence = sentence.replace('▷▷', '')

    print(quotelist)
    print(sentence)
    return sentence
