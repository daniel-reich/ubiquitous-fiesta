
def ascii_sort(lst):
  word1 = lst[0]
  word2 = lst[1]
  word1 = list(word1)
  word2 = list(word2)
  sum1 = 0
  sum2 = 0
  for char in word1:
    sum1 += ord(char)
  for char in word2:
    sum2 += ord(char)
  if sum1 < sum2:
    return "".join(word1)
  else:
    return "".join(word2)

