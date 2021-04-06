
def overlap(word1, word2):
  common = 0
  for i in range(min(len(word1), len(word2))):
    if word1[-(i+1):] == word2[:i+1]:
      common = i+1
  return common
  
def join(lst):
  least = len(lst[0])
  phrase = lst[0]
  for i in range(len(lst)-1):
    common = overlap(lst[i], lst[i+1])
    phrase += lst[i+1][common:]
    if common < least:
      least = common
  return [phrase, least]

