
from collections import OrderedDict
def best_words(lst):
    a = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    highest = OrderedDict()
    for word in lst:
        word_sum = 0
        for letter in word:
            word_sum += a[ord(letter) - 97]
        highest[word] = word_sum
​
    return [v for v in highest if highest.get(v) == max(highest.values())]

