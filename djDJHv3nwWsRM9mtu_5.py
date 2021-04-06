
def validate_spelling(txt):
    txt2 = ''
    for i in txt:
        if i.isalpha():
            txt2 += i
    return txt2[:int(len(txt2)/2)].lower() == txt2[int(len(txt2)/2)::].lower()

