
def does_rhyme(txt1, txt2):
    vowels = "aeiou"
    txt1 = txt1.lower().split()
    txt2 = txt2.lower().split()
    return all([(i in txt1[-1]) == (i in txt2[-1]) for i in vowels])

