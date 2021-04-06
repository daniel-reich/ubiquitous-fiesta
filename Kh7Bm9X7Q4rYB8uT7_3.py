
def is_vowel_sandwich(s):
    return len(s) == 3 and set(s) - set("aeiou") == {s[0], s[2]}

