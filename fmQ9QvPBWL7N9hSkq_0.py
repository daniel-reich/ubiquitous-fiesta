
def unstretch(word):
  return word[0] + ''.join(word[i] for i in range(1,len(word)) if word[i] != word[i-1])

