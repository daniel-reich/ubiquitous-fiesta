
import string
def no_strangers(txt):
    exclude = set(string.punctuation) - set(['\''])
    txt = ''.join(ch for ch in txt if ch not in exclude)
    dic, acquaint, friends = {}, [], []
    for word in txt.split(' '):
        word = word.lower()
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] +=1
            if dic[word] == 3:
                acquaint += [word]
            if dic[word] == 5:
                friends += [word]
                acquaint.remove(word)
​
    return [acquaint, friends]

