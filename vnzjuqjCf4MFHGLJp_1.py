
def shift_letters(txt, n):
    letters = ''.join(i for i in txt if i.isalpha())
    move = -(n % len(letters))
    shifted = iter(letters[move:] + letters[:move])
    return ''.join(
        next(shifted) if t.isalpha() 
        else t for t in txt
    )

