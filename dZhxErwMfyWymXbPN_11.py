
def hangman(phrase, guesses):
    lst = []
    
    for char in phrase:
        if char.isalpha() and (char.lower() or char.upper()) in guesses:
            lst.append(char)
        elif char.isalpha():
            lst.append('-')
        else:
            lst.append(char)
            
    return ''.join(lst)

