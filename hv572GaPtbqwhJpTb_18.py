
import math
​
def elasticize(word):
    length = len(word)
    i = 0
    left = []
    right = []
    while i <= (length / 2 - 1):
        multiplier = i + 1
        left.append(word[i] * multiplier)
        right.append(word[length - i - 1] * multiplier)
        i = multiplier
    
    if length % 2 == 1:
        middle = math.ceil(length / 2)
        left.append(word[middle - 1] * middle)
    
    return ''.join(left + right[::-1])

