
def sum_of_vowels(sentence):
    dic = {"a" : 4, "e" : 3, "i" : 1, "o" : 0, "u" : 0 }
    return sum([dic.get(x.lower(), 0) for x in sentence])

