
from collections import defaultdict
def no_strangers(words):
    counts, acquaintances, friends = defaultdict(int), [], []
    words = words.replace('"','').replace('.','').replace(',','')
    for word in words.lower().split():
        counts[word] += 1
        if counts[word] == 3:
            acquaintances.append(word)
        elif counts[word] == 5:
            friends.append(acquaintances.pop(acquaintances.index(word)))
    return [acquaintances, friends]

