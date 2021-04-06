
def reverse(txt):
  s = ""
​
  for i in reversed(range(len(txt))):
      s += txt[i].swapcase()
​
  return s

