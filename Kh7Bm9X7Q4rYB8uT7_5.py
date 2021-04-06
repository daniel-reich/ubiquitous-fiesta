
def is_vowel_sandwich(s):
    cons=["a","e","i","o","u"]
    if len(s)==3:
        if s[0] not in cons and s[-1]  not in cons:
            if s[1]  in cons:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

