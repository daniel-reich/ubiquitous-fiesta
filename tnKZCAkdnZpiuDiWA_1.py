
def flip_end_chars(txt):
  if not isinstance(txt, str) or len(txt) < 2:
    return 'Incompatible.'
  a, *b, c = txt
  return "Two's a pair." if a == c else ''.join([c]+b+[a])

