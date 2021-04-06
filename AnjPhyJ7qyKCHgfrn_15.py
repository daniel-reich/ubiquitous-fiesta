
def remove_vowels(s):
    vowels = "aeiou"
    for vowel in vowels:
        s = s.replace(vowel, "")
    return s

