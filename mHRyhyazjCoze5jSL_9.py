
def double_swap(txt, c1, c2):
  a = ""
  for letter in txt:
    if letter == c1:
      a += c2
    elif letter == c2:
      a += c1
    else:
      a += letter
  return a

