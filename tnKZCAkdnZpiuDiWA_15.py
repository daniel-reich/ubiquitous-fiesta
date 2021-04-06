
def flip_end_chars(txt):
  if len(txt) < 2:
    return 'Incompatible.'
  elif not isinstance(txt, str):
    return 'Incompatible.'
  elif txt[0] == txt[-1]:
    return 'Two\'s a pair.'
  else:
    return txt[-1] + txt[1:-1] + txt[0]

