
def unrepeated(txt):
  seen = set()
  result = []
  for letter in txt:
    if letter not in seen:
      result.append(letter)
      seen.add(letter)
  return ''.join(result)

