
def sum_of_vowels(sentence):
​
    s = 0
​
    dct = {'A': 4,'E': 3,'I': 1}
​
    for item in sentence:
        s += dct.get(item.upper(), 0)
​
    return s

