
def grouping(w):
    dic = {}
    for word in w:
        caps = 0
        for char in word:
            if char.isupper():
                caps += 1
        if caps in dic:
            dic[caps].append(word)
        else:
            dic[caps] = [word]
​
    for x in dic:
        dic[x] = sorted(dic[x],key = str.lower)
​
    return dic

