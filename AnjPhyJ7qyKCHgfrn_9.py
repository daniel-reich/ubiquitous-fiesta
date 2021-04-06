
def remove_vowels(string):
    vowels = ",".join("aeiou").split(",")
    new_string = ",".join(string.casefold()).split(",")
    for vowel in new_string:
        if vowel in vowels:
            new_string.remove(vowel)
    return "".join(new_string)

