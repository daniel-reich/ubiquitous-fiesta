
import re
​
def translate_word(word):
    if not word:
        return ''
    vowels = 'aeiou'
    capitalized = True if word[0].isupper() else False
    if word[0].lower() in vowels:
        return word + 'yay'
    else:
        i = 1
        while i < len(word) and word[i] not in vowels:
            i += 1
        return (word[i:] + word[:i] + 'ay').capitalize() \
            if capitalized else word[i:] + word[:i] + 'ay'
​
​
def translate_sentence(sentence):
    if not sentence:
        return ''
    lst = sentence.split()
    for i in range(len(lst)):
        begin_word, end_word = -1, len(lst[i])
        for j in range(len(lst[i])):
            if lst[i][j].isalpha():
                if begin_word == -1:
                    begin_word = j
            else:
                if begin_word != -1 and end_word == len(lst[i]):
                    end_word = j
        lst[i] = lst[i][:begin_word] \
            + translate_word(lst[i][begin_word: end_word]) \
            + lst[i][end_word:]
    return ' '.join(lst)

