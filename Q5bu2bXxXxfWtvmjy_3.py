
def missing_letter(txt):
  missing = ''
  for a, b in zip(txt, txt[1:]):
    if ord(b) - ord(a) > 1:
      missing = chr(ord(a) + 1)
  return missing or 'No Missing Letter'

