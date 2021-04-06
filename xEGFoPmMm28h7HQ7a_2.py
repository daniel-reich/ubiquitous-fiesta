
from itertools import product
def letter_combinations(digits):
    digits_to_chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                       '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return [''.join(c for c in x) for x in product(*[digits_to_chars[d]
                                                     for d in digits])]

