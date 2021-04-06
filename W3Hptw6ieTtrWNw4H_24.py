
import string
def bifid(text):
    t = text.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').upper()
    d = {'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 'F': '21', 'G': '22', 'H': '23', 'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55', 'I': '24', 'J': '24', ' ': ' '}
    e = {'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e', '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'k', '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p', '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u', '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'}
​
    if ' ' in  text:
        a = ''.join([d[x] for x in t])
        b = a[0::2] + a[1::2]
        c = [b[x:x+2] for x in range(0,len(b),2)]
        return ''.join([e[x+y] for x,y in c])
    else:
        a = ''.join([d[x] for x in text.upper()])
        b = zip(a[:len(t)], a[len(t):])
        return ''.join([e[x+y] for x,y in b])

