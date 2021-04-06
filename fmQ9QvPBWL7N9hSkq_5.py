
def unstretch(word):
  term = word[0]
  count = 0
  
  for letter in word:
    if term[count] is not letter:
      term+=letter
      count+=1
  return term

