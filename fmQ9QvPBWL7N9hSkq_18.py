
def unstretch(word):
  return word[0] + "".join([word[x] for x in range(1, len(word)) if word[x] != word[x-1]])

