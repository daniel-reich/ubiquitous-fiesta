
def same_upsidedown(txt):
  for n, num in zip(txt, txt[::-1]):
    if n == num and n != "0":
      return False
  return True

