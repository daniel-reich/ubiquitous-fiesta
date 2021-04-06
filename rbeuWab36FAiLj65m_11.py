
def count_caps(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    return count
​
def grouping(lst):
    dict = {}
    for word in lst:
        if count_caps(word) in dict:
            dict[count_caps(word)].append(word)
        else:
            dict[count_caps(word)] = [word]
​
    sortedDict = {}
    for k,v in sorted(dict.items()):
        sortedDict[k] = sorted(v, key=lambda x:x.upper())
​
    return sortedDict

