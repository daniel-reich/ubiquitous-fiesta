
def almost_palindrome(txt):
  c = list(txt)
  for i, r in enumerate(range(len(txt)-1,-1,-1)):
    if txt[i] != txt[r]:
      c[r] = txt[i]
      break
  return c[::-1] == c if txt[::-1] != txt else False

