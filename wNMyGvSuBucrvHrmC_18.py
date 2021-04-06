
def number_of_repeats(s):
    chars = ''
​
    for c in s:
        chars += c
        if len(s) % len(chars) == 0 and len(chars) > 1:
            return s.count(chars)

