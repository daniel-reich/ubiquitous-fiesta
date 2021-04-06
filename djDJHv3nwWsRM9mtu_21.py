
def validate_spelling(txt):
    s = txt.split()
    word = ""
    correct_spelling = s[-1][:-1]
    for x in s[:-1]:
        x = x.replace(".", "")
        word += x.lower()
    return word.capitalize() == correct_spelling

