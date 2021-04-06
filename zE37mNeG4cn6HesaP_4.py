
def max_ham(s1, s2):
  anagram = False
  if "".join(sorted(s1)) == "".join(sorted(s2)):
    anagram = True
  if anagram is True:
    hamming = 0
    for index,c in enumerate(s1):
      if s2[index] !=c:
        hamming = hamming +1
    if hamming == len(s1):
      return True
    else:
      return hamming
  else:
    return False

