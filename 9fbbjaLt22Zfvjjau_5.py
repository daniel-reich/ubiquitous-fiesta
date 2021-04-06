
import re
def paul_cipher(txt):
    txt= txt.capitalize()    
    a = re.findall(r'[a-zA-Z]',txt)
    ans = [a[0]]    
    for i,w in enumerate(a[1:]):
        n = ord(w.lower()) -96 + ord(a[i].lower()) -96
        if n>26:n-=26
        ans.append(chr(int(n)+96).upper())    
    return ''.join(list(map(lambda x: ans.pop(0) if x.isalpha() else x,list(txt)))).upper()

