
ps = {'A':11,'B':12,'C':13,'D':14,"E":15,'F':21,'G':22,'H':23,'I':24,'J':24,'K':25,'L':31,
        'M':32,'N':33,'O':34,'P':35,'Q':41,'R':42,"S":43,"T":44,"U":45,'V':51,'W':52,'X':53,"Y":54,'Z':55
    }
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def polybius(text):
    if(text[0].isdigit()==False):return enc(text)
    return dec(text)
​
def dec(text):
    text = text.split(' ')
    ans =  list(list(get_key(ps,int(i[j]+i[j+1])).lower() if i[j]+i[j+1]!='24' else 'i'  for j in range(0,len(i),2)) for i in text )
    return ' '.join(list(''.join(i) for i in ans))
def enc(text):
    text = ''.join(list(i for i in text if ord(i)<123 and ord(i)>64 or i==' '))
    print(get_key(ps, 11))
    return "".join(list(str(ps[i.upper()]) if i!= ' ' else i for i in text ))

