
def is_vowel_sandwich(mystr):
    vowels = 'aeiou'
    if len(mystr) == 3:
        if mystr[0] not in vowels:
            if mystr[-1] not in vowels:
                if mystr[1] in vowels:
                    return True
    return False

