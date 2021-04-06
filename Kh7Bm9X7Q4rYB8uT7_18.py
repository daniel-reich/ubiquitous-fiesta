
def is_vowel_sandwich(s):
    if len(s)!=3:
        return False
    a="aeiou"
    return s[0] not in a and s[2] not in a and s[1] in a

