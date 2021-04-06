
def is_sorted(words, alphabet):
  code = {ch: i for i, ch in enumerate(alphabet)}
  for i in range(len(words)-1):
    w2l = len(words[i+1])
    for j in range(len(words[i])):
      if j == w2l or code[words[i][j]] > code[words[i+1][j]]:
        return False
      if code[words[i][j]] < code[words[i+1][j]]:
        break
  return True

