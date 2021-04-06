
def remove_vowels(string):
    vowels = "aeiou"
    for vowel in vowels:
        string = string.replace(vowel, "")
    return string

