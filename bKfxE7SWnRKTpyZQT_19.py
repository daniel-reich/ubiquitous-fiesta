
def replace_vowel(word):
    if 'a' in word:
        word=word.replace('a','1')
    if 'e' in word:
        word=word.replace('e','2')
    if 'i' in word:
        word=word.replace('i','3')
    if 'o' in word:
        word=word.replace('o','4')
    if 'u' in word:
        word=word.replace('u','5')
    return word

