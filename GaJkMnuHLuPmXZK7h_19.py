
def letters(word1, word2):
  outputlist = ["", "", ""]
  shared = ""
  u1 = ""
  u2 = ""
​
  for letter in word1:
      if letter not in shared:
          if letter in word2:
              shared += letter
      if letter not in u1:
         if letter not in word2:
              u1 += letter
  if letter not in u2:
      for letter in word2:
          if letter not in word1:
              u2 += letter
​
  outputlist[0] += "".join(sorted(shared))
  outputlist[1] += "".join(sorted(u1))
  outputlist[2] += "".join(sorted(u2))
​
  return outputlist

