
def true_alphabetic(txt):
  s_txt = ''.join(sorted(txt.replace(' ', '')))
  for i, x in enumerate(txt):
    if x == ' ':
      s_txt = s_txt[:i] + ' ' + s_txt[i:]
  return s_txt

