
def almost_palindrome(txt):
  l = len(txt)//2
  if l % 2:
    return sum(1 for x, y in zip(txt[l+1:][::-1], txt[:l]) if x != y) == 1
  return sum(1 for x, y in zip(txt[l:][::-1], txt[:l]) if x != y) == 1

