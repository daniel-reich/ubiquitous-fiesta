
from collections import OrderedDict
def keyword_cipher(key, message):
    ans=''
    s=''.join([i for i in key]+[chr(j) for j in range(97,123) if chr(j) not in key])
    s=''.join(OrderedDict.fromkeys(s))
    for i in message:
        if ord(i) not in range(97,123):
            ans+=i
        else:
            ans+=s[ord(i)-97]
    return ans

