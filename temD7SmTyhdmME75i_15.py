
def to_boolean_list(word):
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  ans = []
  for i in list(word):
    if i in alphabet:
      if alphabet.index(i) % 2 == 0:
        ans.append(True)
      else:
        ans.append(False)
  return ans

