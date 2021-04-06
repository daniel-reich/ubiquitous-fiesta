
def pig_latin(txt):
    vowels = 'AaEeIiOoUu'
    attempt = " ".join([i+'way' if i[0] in vowels else i[1:]+i[0].lower()+"ay" for i in txt[:-1].split()])+txt[-1]
    return attempt.capitalize()

