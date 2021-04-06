
def unstretch(word):
  k = ""
  k += word[0]
  i = 1
  while i < len(word):
    if word[i] != word[i-1]:
      k += word[i]
    
    i += 1
  return k

