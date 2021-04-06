
def capital_letters(txt):
    capital_counter = 0
    for letter in txt:
        if letter.isupper():
            capital_counter +=1
    return capital_counter

