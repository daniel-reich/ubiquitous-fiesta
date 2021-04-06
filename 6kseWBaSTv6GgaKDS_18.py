
def next_letters(s):
    res, add_on = '', 1
    for c in s[::-1]:
        res += chr((ord(c) - 65 + add_on) % 26 + 65)
        add_on = 1 if c == 'Z' and add_on == 1 else 0
    if add_on == 1:
        res += 'A'
    return res[::-1]

