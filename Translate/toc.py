#DEVELOPER : AnastasiosZ

import random

QUOTECHAR = '|'
BASE26CHAR = '°'

# def R2SPACES(s):
#     #Removing 2+ consecutive spaces
#     #using recursion, admitedly less smart

#     if "  " in s:
#         return s.replace("  ", "")
#     else:
#         return s


def RAND():

    #Shitty random function

    return random.randint(random.randint(1, 5), random.randint(5, 8))


def addDiaretics(char, nec):
    #Adding diacritics to valid letters

    a = ["à", "á", "â", "ä"]
    e = ["è", "é", "ê", "ë"]
    i = ["î", "í", "ì"]
    o = ["ô", "ó", "ò", "ö"]
    u = ["ü", "ù", "ú", "û"]
    y = ["ý"]
    c = ["č", "ć"]
    r = ["ř"]
    s = ["š", "ś"]
    n = ["ň", "ń"]
    d = ["đ"]
    l = ["ł"]
    g = ["ğ"]
    z = ["ž", "ź"]

    if nec == True:
        return random.choice(o)
    if random.randint(0, 10) >= 3:
        return char

    if char == 'a':
        return random.choice(a)
    elif char == 'e':
        return random.choice(e)
    elif char == 'i':
        return random.choice(i)
    elif char == 'o':
        return random.choice(o)
    elif char == 'u':
        return random.choice(u)
    elif char == 'y':
        return random.choice(y)
    elif char == 'c':
        return random.choice(c)
    elif char == 'r':
        return random.choice(r)
    elif char == 's':
        return random.choice(s)
    elif char == 'n':
        return random.choice(n)
    elif char == 'd':
        return random.choice(d)
    elif char == 'l':
        return random.choice(l)
    elif char == 'g':
        return random.choice(g)
    elif char == 'g':
        return random.choice(z)
    else:
        return char


def resolveQuotes(s):

    #If a quote character exists in a string
    #to take care of multiple quotes i need to search each time because the string changes
    quoteIndeces = []

    if QUOTECHAR in s:
        for char in range(len(s)):
            if s[char] == QUOTECHAR:
                quoteIndeces.append(char)
                if len(quoteIndeces) == 2:
                    break

        index1 = quoteIndeces[0]
        index2 = quoteIndeces[1]

        #using recursion to take care of multiple quotes -> smart kinda

        return resolveQuotes(s[:index1] + ' "' +
                             handleSentences(s[index1 + 1:index2]) + '" ' +
                             s[index2 + 1::])

    else:
        return s


def trueLen(s):
    #Checking if last characters of a word are numeric and counting all of it as one character

    num = False
    final = 0
    for char in range(len(s)):
        if s[char] >= '1' and s[char] <= '9':
            if num == False:
                num = True
        else:
            if num == True:
                num = False
                final += 1
            final += 1
    if num == True:
        return final + 1
    else:
        return final


def trueLast(s):
    #Finding the start point of the numeric character such that we remove it afterwards

    final = len(s) - 1
    while ((s[final] >= '1' and s[final] <= '9') and final > 0):
        final -= 1
    if s[-1] >= '1' and s[-1] <= '9':
        return final + 1
    else:
        return final


def CONV(n):

    #Converting the length of a string into a base 26 number

    if (n > 26):
        final = chr(n % 26 + 96) + BASE26CHAR
        n = n // 26
        while n > 0:
            final = chr(n % 26 + 96) + BASE26CHAR + final
            n = n // 26
        return final
    else:
        return chr(n % 26 + 96)


def ISNUMERIC(s):

    #Checking if entire word is numerical

    for x in range(len(s)):
        if s[x] < '0' or s[x] > '9':
            return False
    return True


def toCocanb(s):

    #Separating each sentence into words (separated by spaces) and removing their last
    #letter and adding it to the end of the sentence after the separator "non"

    words = s.split(' ')
    final1 = ""
    final2 = ""
    endl = []
    endn = []

    #Making sure that we are only dealing with shit outside the quote

    q = False

    #Iterate with each word, if i find a QUOTECHAR at the start, i ignore everything until
    #i find a QUOTECHAR at the end

    for word in words:
        #if entire word is consisted of spaces remove it
        if len(word) == 0 or word == ' ' * len(word):
            continue

        if not q:

            #NOT IN QUOTES

            if word[0] == '"':
                q = True
                final1 += word
            else:
                #if entire word is a number skip it

                if ISNUMERIC(word) == True:
                    final1 += word

                #carrying out separation

                else:
                    endl.append(trueLast(word))
                    endn.append(trueLen(word))
                    final1 += word[:endl[-1]]
                    final2 += word[endl[-1]::] + CONV(endn[-1])
        else:
            final1 += word
            if word[-1] == '"':
                q = False

    #Adding diacritics
    q = False
    #making sure i dont add diacritics to a quote

    temp1 = list(final1)

    for x in range(len(temp1)):
        if not q:
            if temp1[x] == '"':
                q = True
            else:
                temp1[x] = addDiaretics(temp1[x], False)
        else:
            if temp1[x] == '"':
                q = False

    temp2 = list(final2)
    for x in range(len(temp2)):
        temp2[x] = addDiaretics(temp2[x], False)

    #Concatenating before-separator and after-separator strings
    #and adding necessary diaretics to any non-seperator non
    #addition of "diaretics" is done only outside quotes

    q = False

    final = ''.join(temp1) + "non" + ''.join(temp2)
    nonO = False

    for x in range(len(final), 2, -1):
        if not q:
            if final[x - 2] == '"':
                q = True
            else:
                if final[x - 3:x] == "non":
                    if nonO == False:
                        nonO = True
                    else:
                        temp = list(final)
                        temp[x - 2] = addDiaretics("o", True)
                        final = ''.join(temp)
        else:
            if final[x - 2] == '"':
                q = False

    #Adding spaces to random places
    i = RAND()
    while (i < len(final)):
        final = final[:i] + " " + final[i::]
        i += RAND()

    #Capitalizing the first letter of each sentence

    return final[0].upper() + final[1::]


def handleSentences(s):

    final = ""

    sens = []
    punc = []
    prev = 0

    # Check for quotes

    s = resolveQuotes(s)

    #Adding a period at the end of the sentence not having any punctuation

    # if(len(s)==1):
    #     punc.append('.')
    # else:
    #     for x in range(len(s)-1,0,-1):
    #         if s[x] != ' ':
    #             if s[x] not in ['.','?','!']:
    #                 s = s + '.'
    #             break

    q = False

    #Seperating the sentences by punctuation
    #i include the entirety of the quote in the sentence and will deal with it in toCocanb
    prev = 0

    for x in range(len(s)):
        if not q:
            if s[x] == '"':
                q = True
            else:
                if s[x] == '.' or s[x] == '?' or s[x] == '!':
                    punc.append(s[x])
                    sens.append(s[prev:x])
                    prev = x + 1
        else:
            if s[x] == '"':
                q = False

    sens.append(s[prev::])

    #Concatenating cocanb equivalent of sentences

    i = 0

    for sen in sens:

        if (len(sen.replace(' ' * len(sen), ''))) == 0:
            continue
        if (len(sen) == 1):
            if i < len(punc):
                final = final + toCocanb(sen) + punc[i] + " "
            else:
                final = final + toCocanb(sen)
        else:
            if i < len(punc):
                final = final + toCocanb(sen[0].upper() +
                                         sen[1::]) + punc[i] + " "
            else:
                final = final + toCocanb(sen[0].upper() + sen[1::])
        i += 1

    #return final concatenation of all now cocanb sentences

    return final
