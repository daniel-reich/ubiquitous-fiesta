
def char_appears(sentence, char):
  arr = sentence.lower().split()
  ans = []
  for el in arr: ans.append(el.count(char))
  return ans

