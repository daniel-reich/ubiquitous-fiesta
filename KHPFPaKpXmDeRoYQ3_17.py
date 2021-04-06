
def check_score(s):
    symbol_lookup = {'#': 5, 'O': 3, 'X': 1,
                     '!': -1, '!!': -3, '!!!': -5}
    total = sum(symbol_lookup[ch] for ch in sum(s, []))
    return 0 if total < 0 else total

