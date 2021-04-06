
def split(txt):
  cnt, word, res = 0, '', []
  for c in txt:
    word += c
    cnt += 1 if c == '(' else -1
    if cnt == 0:
      res.append(word)
      word = ''
  return res

