
def alternating_caps(txt):
  result, toggle = '', True
  for letter in txt:
    if not letter.isalpha():
      result += letter
      continue
    result += letter.upper() if toggle else letter.lower()
    toggle = not toggle
  return result

