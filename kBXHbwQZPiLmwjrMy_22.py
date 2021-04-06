
import re
​
def translate_word(word):
    vowels = 'aeiou'
    vowelind = []
    for tchar in vowels:
        ind = word.lower().find(tchar)
        if ind>-1:
            vowelind.append(ind)
    if len(vowelind)==0:
        return word
    fwi = min(vowelind) #first vowel index
    if fwi == 0:
        anotherword = word+"yay"
    else:
        anotherword = word[fwi:]+word[0:fwi]+"ay"
    anotherword = anotherword.lower()
    if word[0].isupper():
        anotherword=anotherword[0].upper()+anotherword[1:]
    return anotherword
​
​
​
​
def translate_sentence(sentence):
    translated = ""
    words = re.split('(\W+)', sentence)
    for w in words:
        if w.isalpha():
            translated += translate_word(w) 
        else:
            translated += w
    return translated

