
def split(txt):
    new_sentence = ""
    for char in txt:
        if is_vowel(char):
            new_sentence += char
​
    for char in txt:
        if not is_vowel(char):
            new_sentence += char
​
    return new_sentence
​
​
def is_vowel(character):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    if character in vowels:
        return True
    return False

