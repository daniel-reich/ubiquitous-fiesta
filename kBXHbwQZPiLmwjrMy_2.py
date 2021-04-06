
def translate_word(w):
  if w:
    word = ''.join(i for i in w if i.isalpha())
    if word[0] in 'aeiouAEIOU':
      pLatin = word + 'yay'
    else:
      cap = True if word[0].isupper() else False
      for i in range(len(word)):
        if word[i] in 'aeiou':
          ndx = i; break
      pLatin = word[ndx:]+word[:ndx]+'ay'
      pLatin = pLatin.title() if cap else pLatin
    return w.replace(word,pLatin)
  return ''
​
def translate_sentence(sentence):
  return ' '.join(translate_word(i) for i in sentence.split())

