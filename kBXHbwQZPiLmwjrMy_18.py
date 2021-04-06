
import re
​
​
def translate_word(word):
    vowels = re.compile("[aeiou]")
    pattern = re.compile("\W")
    punctuation = []
    if not word:
        return word
    letters = []
    for char in word:
        if pattern.match(char):
            punctuation += [word.index(char), char]
        else:
            letters += [char]
    if letters:
        word = ''.join(letters)
    caps = False
    if word[0].isupper():
        caps = True
        word = word.lower()
    if vowels.match(word):
        word = word + "yay"
    else:
        while not vowels.match(word):
            word = word[1:] + word[0]
        word = word + "ay"
    if caps:
        word = word.capitalize()
    if punctuation:
        if not punctuation[0]:
            word = punctuation[1] + word
        elif len(punctuation) > 2:
            word = word + punctuation[1] + punctuation[-1]
        else:
            word = word + punctuation[1]
    return word
​
​
def translate_sentence(sentence):
    words = sentence.split()
    translated = []
    for word in words:
        translated += [translate_word(word)]
    return " ".join(translated)

