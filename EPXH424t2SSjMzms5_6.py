
def remix(txt, lst):
  word = list(txt)
  newWord = list(txt)
  for i in range(len(txt)):
    newWord[lst[i]] = word[i]
  ans = ''.join(newWord)
  return ans

