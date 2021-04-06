
def grant_the_hint(txt):
  ltxt = txt.split()
  m = max(len(i) for i in ltxt)
  return [' '.join([letter(i, j) for i in ltxt]) for j in range(m+1)]
​
def letter(string, index):
  return string[:index] + '_' * (len(string) - index)

