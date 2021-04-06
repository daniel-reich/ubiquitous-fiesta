
from re import sub, search
​
def translate_word(word):
    if not word: return ''
    word = word if isinstance(word, str) else word.group()
    if word[0] in 'aeiouAEIOU':
        return word +'yay'
    pre, su = search(r'([^aeiouAEIOU]+)(.+)', word).groups()
    return su+pre+'ay' if word.islower() else (su+pre+'ay').capitalize()
​
def translate_sentence(txt):
    return sub(r'\w+', translate_word, txt)

