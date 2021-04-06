
def is_vowel_sandwich(s):
    x = "aeiouAEIOU"
    if len(s) == 3:
        if list(s)[0] not in x and list(s)[-1] not in x:
            if list(s)[1] in x:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

