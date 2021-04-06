
def flip_end_chars(txt):
  if not isinstance(txt, str) or len(txt) < 2: return "Incompatible."
  if txt[-1] == txt[0]: return "Two's a pair."
  s = ""
  s += txt[-1]
  s += txt[1:-1]
  s += txt[0]
  return s

