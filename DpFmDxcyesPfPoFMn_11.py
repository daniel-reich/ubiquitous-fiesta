
def get_13(lst, novalid=True):
    a = [b*3 if a % 2 else b for a, b in enumerate(lst)]
    if not sum(a) % 10: return 'Valid'
    if novalid:
        return lst[:-1] + [10 -sum(a) % 10] if lst[-1] == 10 else lst[:-1] + [lst[-1] + 10-sum(a)%10] if 10 - sum(a) % 10 < sum(a) % 10 else  lst[:-1] + [lst[-1] - sum(a)%10]
​
def isbn13(txt):
    if len(txt) == 10:
        digits = [10 if x == 'X' else int(x) for x in txt ]
        return ''.join(map(str, get_13([9, 7, 8] + digits[:]))) if not sum([i*x for i, x in enumerate(digits[::-1], 1)]) % 11 else 'Invalid'
    else:
        return get_13([int(x) for x in txt], novalid=False) or 'Invalid'

