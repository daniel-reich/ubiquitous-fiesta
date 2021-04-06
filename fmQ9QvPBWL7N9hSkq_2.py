
def unstretch(word):
  return ''.join([word[0]] + [word[i] for i in range(1,len(word)) if word[i]!=word[i-1]])

