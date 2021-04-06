
def hangman(phrase, lst):
    s =''
    for char in phrase:
        if char.isdigit() or not char.isalpha():s+=char
        elif char.lower() in lst:s+=char
        elif char==' ':s+=' '
        else:s+='-'
    return s

