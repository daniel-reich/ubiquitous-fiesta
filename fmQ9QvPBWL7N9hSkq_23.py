
def unstretch(word):
  l = ""
  
  for i in word:
    if i not in l:
      l = l+i
    elif i in l:
      if l[-1] != i:
        l = l+i
  return l

