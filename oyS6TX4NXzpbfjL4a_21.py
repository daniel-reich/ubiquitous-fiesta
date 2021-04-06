
VALUE = { 'r': 1, 'd': 2, 'n': 1, 'g': 2, 'c': 3, 'p': 3, 'h': 4, 's': 1,
    'w': 4, 'y': 4, 'b': 3, 'e': 1, 'q': 10, 't': 1, 'u': 1, 'x': 8, 'l': 2,
    'i': 1, 'f': 4, 'j': 8, 'a': 1, 'k': 5, 'z': 10, 'm': 3, 'o': 1, 'v': 4 }
​
def best_start(lst, word):
    func = {'-': lambda ch: VALUE[ch],
            'DL': lambda ch: VALUE[ch] * 2,
            'TL': lambda ch: VALUE[ch] * 3,
            'DW': lambda ch: wrd_val }
​
    def get_value(i0):
        return sum(func[code](ch) for code, ch in zip(lst[i0:], word))
        
    wrd_val = sum(VALUE[c] for c in word)
    return max(range(len(lst)-len(word)), key = get_value)

