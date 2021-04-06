
def find_letters(word):
  ans = []
  for x in word:
    if word.count(x) <= 1:
      ans.append(x)
  return ans

