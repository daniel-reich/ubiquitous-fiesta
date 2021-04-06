
def ascii_sort(lst):
  word1 = sum([ord(i) for i in lst[0]])
  word2 = sum([ord(i) for i in lst[1]])
  return lst[0] if word1 < word2 else lst[1]

