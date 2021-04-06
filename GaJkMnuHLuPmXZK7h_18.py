
def letters(word1, word2):
  result = ['', '', '']
  for i in word1:
    if i in word2:
      result[0]+=i
    else:
      result[1]+=i
  for i in word2:
    if i not in word1:
      result[2]+=i
  return [''.join(sorted(set(i))) for i in result]

