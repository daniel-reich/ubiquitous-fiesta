
def isbn10(n):
    try:
        digits = int(n[:-1])
    except ValueError:
        return "Invalid"
    S = 10 if n[-1] == 'X' else int(n[-1])
    factor = 1
    for digit in n[:-1][::-1]:
        factor += 1
        S += int(digit) * factor
    if S % 11 != 0:
        return "Invalid"
    n = "978" + n[:-1]
    S = 0
    factor = 1
    for digit in n:
        S += int(digit) * factor
        factor = 1 if factor == 3 else 3
    S %= 10
    n += str(10 - S)
    return n
    
def isbn13(txt):
    n = txt
    L = len(txt)
    if L not in [10, 13]:
        return "Invalid"
    if L == 10:
        return isbn10(txt)
    try:
        digits = int(n[:-1])
    except ValueError:
        return "Invalid"
    S = 10 if n[-1] == 'X' else int(n[-1])
    factor = 1
    for digit in n[:-1]:
        S += int(digit) * factor
        factor = 1 if factor == 3 else 3
    return "Valid" if S % 10 == 0 else "Invalid"

