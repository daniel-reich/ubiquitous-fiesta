
def pig_latin_sentence(sentence):
  return ' '.join([pl(i) for i in sentence.split()])
  
def pl(word):
  if word[0] in 'aeiou':
    return word+'way'
  lst = [i for i in range(len(word)) if word[i] in 'aeiou']
  return word[lst[0]:]+word[:lst[0]]+'ay'

