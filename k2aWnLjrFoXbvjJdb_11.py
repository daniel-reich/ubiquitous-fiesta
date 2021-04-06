
import string
kk = string.ascii_uppercase
key = [[kk[(i+j)%len(kk)] for i in range(len(kk))] for j in range(len(kk))]
def vigenere(txt,keyword):
    global key
    if ' ' in txt:
        return encode(txt, keyword)
    return decode(txt, keyword)
​
​
​
def encode(txt,keyword):
    global key
    res = ''
    txt = txt.replace(' ','')
    for i in string.punctuation:
        txt = txt.replace(i,'')
    txt = txt.upper()
    keystr = ''.join([keyword[i%len(keyword)].upper() for i in range(len(txt))])
    for x,y in zip(txt,keystr):
        y_index = 0
        for i in range(len(key)):
            if key[i][0] == y:
                y_index = i
​
        res += key[y_index][key[0].index(x)]
​
    return res
​
def decode(txt,keyword):
    global key
    res = ''
    keystr = ''.join([keyword[i % len(keyword)].upper() for i in range(len(txt))])
    for x,y in zip(txt,keystr):
        y_index = 0
        for i in range(len(key)):
            if key[i][0]==y:
                y_index = i
        x_index = 0
        for j in range(len(key[0])):
            if key[y_index][j]==x:
                x_index = j
        res+=key[0][x_index]
    return res

