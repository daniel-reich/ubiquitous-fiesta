
def sentence(words):
  newlist = []
  newlist2 = []
  for i in range(len(words)):
    if i+1 == len(words)-1:
      x = starts_with_vowel(words[i])
      y = starts_with_vowel(words[i+1])
      newlist2.append(x)
      newlist2.append(y)
      z = ' and '.join(newlist2)
      newlist.append(z)
      break
    else:
      newlist.append(starts_with_vowel(words[i]))
  return '{}.'.format(', '.join(newlist).capitalize())
​
def starts_with_vowel(word):
  newlist = []
  vowels = 'aeiouAEIOU'
  if word[0] in vowels:
    newlist.append('an')
    newlist.append(word)
  else:
    newlist.append('a')
    newlist.append(word)
  return ' '.join(newlist)

