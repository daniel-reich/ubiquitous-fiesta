
import re
def increasing_word_weights(s):
    s = re.sub(r'[^a-zA-Z\s]','',s).split(' ')
    s = list(map(lambda x:sum(list(map(lambda y:ord(y),x))), s))
    for i in range(1,len(s)):
        if s[i]<=s[i-1]:return False
    return  True

