
def flip_end_chars(txt):
  if type(txt).__name__ != "str" or len(txt) < 2: return "Incompatible."
  res = txt[-1] + txt[1:-1] + txt[0]
  if res == txt: return "Two's a pair."
  return res

