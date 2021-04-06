
def first_repeat(chars):
    for i, char in enumerate(chars):
        if i < len(chars) and chars[i] in chars[i+1:]:
            return chars[i]
    return '-1'

