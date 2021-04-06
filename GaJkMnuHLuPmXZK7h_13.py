
def letters(word1, word2):
  s, u1, u2 = '','',''
  for i in word1:
    if i in word2:
      if i not in s:
        s += i
    else:
      if i not in u1:
        u1 += i
  for i in word2:
    if i not in word1:
      if i not in u2:
        u2 += i
  return [''.join(sorted(s)), ''.join(sorted(u1)), ''.join(sorted(u2))]

