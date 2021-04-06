
def replace_vowel(word):
    new_word = ""
    vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    for i in word:
        if i in vowels:
            new_word = new_word + str(vowels.get(i, 0))
        else:
            new_word = new_word + i
    return new_word

