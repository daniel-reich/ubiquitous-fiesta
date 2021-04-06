
def is_icecream_sandwich(txt):
  return sum(txt[i] != txt[i - 1] for i in range(1, len(txt))) == 2 and len(set(txt)) == 2 and txt == txt[::-1]

