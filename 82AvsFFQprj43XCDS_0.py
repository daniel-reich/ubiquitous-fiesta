
from collections import defaultdict
​
def no_strangers(txt):
    d = defaultdict(int)
    acquaintance, friend = [], []
​
    for word in txt.lower().split():
        word = word.strip('".,')
        d[word] += 1
        if d[word] == 3:
            acquaintance.append(word)
        elif d[word] == 5:
            friend.append(word)
            acquaintance.remove(word)
​
    return [acquaintance, friend]

