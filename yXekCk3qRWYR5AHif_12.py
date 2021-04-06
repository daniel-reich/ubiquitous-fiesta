
def vow_replace(word,vowel):
    word=str(word)
    for i in word:
        if i in "aeiou":
            word=word.replace(i,vowel)
    return word

