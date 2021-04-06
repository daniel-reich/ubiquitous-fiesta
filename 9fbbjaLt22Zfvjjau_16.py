
from string import ascii_uppercase as l
l = [c for c in l*2]
def paul_cipher(s):
  new_s = ""
  prev_c = ""
  for c in s:
    c = c.upper()
    if c in l:
      if prev_c != "":
        idx = l.index(c) + l.index(prev_c) + 1
        new_s += l[idx]
        prev_c = c
      else:
        new_s += c
        prev_c = c
    else:
      new_s += c
  return new_s

