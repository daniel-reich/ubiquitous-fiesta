
def unstretch(word):
  a = [v for i, v in enumerate(word) if i == 0 or v != word[i-1]]
  return "".join(a)

