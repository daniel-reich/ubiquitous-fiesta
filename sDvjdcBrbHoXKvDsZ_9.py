
def anagram(name, words):
  newname = sorted(''.join(name.split()).lower())
  newwords = sorted(''.join(words).lower())
  return newwords == newname

