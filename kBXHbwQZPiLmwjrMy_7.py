
import re
​
def translate_word(word):
    if not word:
        return ''
    if word[0] not in 'aeiouAEIOU':
        i = re.search('[aeiouAEIOU]', word).start()
        res = word[i:] + word[:i] + "ay"
        if word[0].isupper():
            res = res[0].upper() + res[1:].lower()
    else:
        res = word + 'yay'
    return res
  
​
def translate_sentence(sentence):
    return re.sub(r'\w+', lambda w: translate_word(w.group(0)), sentence)

