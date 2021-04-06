
def insert_whitespace(txt):
  pos = []
  for idx, c in enumerate(txt):
    if c.isupper():
      pos += [idx]
  pos += [len(txt)]
  return ' '.join(txt[pos[i]: pos[i + 1]] for i in range(len(pos) - 1))

