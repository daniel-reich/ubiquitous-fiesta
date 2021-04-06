
def neighboring(txt):
  return all(abs(ord(txt[x]) - ord(txt[x + 1])) == 1 for x in range(len(txt) - 1))

