
def count_repetitions(lst):
    s = list(set(lst))
    res ={}
    for word in s:
        res[word]=lst.count(word)
    return res

