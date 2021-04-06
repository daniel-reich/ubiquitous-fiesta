
from itertools import product
​
def letter_combinations(digits):
    conversion = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], 
    '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
    }
    return [''.join(x) for x in list((product(*[conversion[c] for c in digits])))]

