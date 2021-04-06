
def does_rhyme(txt1, txt2):
    import re
    return re.findall(r'\w+', txt1.lower())[-1][-2:] == re.findall(r'\w+', txt2.lower())[-1][-2:]

