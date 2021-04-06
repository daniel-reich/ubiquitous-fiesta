
value = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
def sum_of_vowels(s):
    return sum(value[c] for c in s.upper() if c in value)

