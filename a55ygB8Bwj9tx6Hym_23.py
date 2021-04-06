
def steps_to_convert(txt):
    txt = list(txt)
    total = len(txt)
    lower = 0
    upper = 0
    for i in txt:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    if upper >= lower:
        return total - upper
    elif lower > upper:
        return total - lower

