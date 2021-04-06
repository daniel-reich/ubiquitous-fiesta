
def capitlise_end(w):
  return w[:-1] + chr(ord(w[-1])-32) if 'a' <= w[-1] <= 'z' else w
​
def cap_last(txt):
  return ' '.join(capitlise_end(w) for w in txt.split(' '))

