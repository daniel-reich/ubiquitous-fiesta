
def special_reverse_string(txt):
    up = []
    space = []
    for i in range(len(txt)):
        if txt[i].isupper():
            up.append(i)
        elif txt[i] == ' ':
            space.append(i)
    reverse = list(txt.replace(' ','').lower()[::-1])
    for i in space:
        reverse.insert(i," ")
    for i in up:
        reverse[i] = reverse[i].upper()
    return ''.join(reverse)

