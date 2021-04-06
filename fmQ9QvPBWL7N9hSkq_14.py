
def unstretch(word):
  m = ''
  for i in range(len(word)-1):
    if word[i]!=word[i+1]:
      m+=word[i]
  return m+word[-1]

