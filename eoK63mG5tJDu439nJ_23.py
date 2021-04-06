
def isWordChain(words):
  for i in range(len(words)-1):
    if len(words[i]) == len(words[i+1]):
      diff  = 0
      for j in range(len(words[i])):
        if words[i][j] != words[i+1][j]: diff += 1
      if diff != 1: return False
    if len(words[i]) < len(words[i+1]):
      if len(words[i])+1 == len(words[i+1]) and words[i] in words[i+1]:
        continue
      elif len(words[i])+1 != len(words[i+1]): return False
      else:
        diff = 0
        for j in range(len(words[i+1])):
          if words[i][j-diff] != words[i+1][j]:
            diff += 1
        if diff != 1: return False
    if len(words[i]) > len(words[i+1]):
      if len(words[i])-1 == len(words[i+1]) and words[i+1] in words[i]:
        continue
      elif len(words[i])-1 != len(words[i+1]): return False
      else:
        diff = 0
        for j in range(len(words[i])):
          if words[i][j] != words[i+1][j-diff]:
            diff += 1
        if diff != 1: return False
  return True

