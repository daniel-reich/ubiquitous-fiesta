
def get_pattern(txt):
  c, patt, codes = 0, [], {}
  for k in txt:
    if not k in codes:
      codes[k] = c
      c += 1
    patt.append(codes[k])
  return patt
​
def same_letter_pattern(txt1, txt2):
  return get_pattern(txt1) == get_pattern(txt2)

