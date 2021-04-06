
def same_letter_pattern(txt1, txt2):
    return len(txt1) == len(txt2) and len(set(zip(txt1,txt2))) == len(dict(zip(txt1, txt2)))

