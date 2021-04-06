
def is_icecream_sandwich(txt):
  if len(txt) < 3 or len(set(txt)) != 2:
    return False
  return txt.count(txt[0]) % 2 == 0

