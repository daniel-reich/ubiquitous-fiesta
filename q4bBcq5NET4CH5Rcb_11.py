
def jay_and_bob(txt):
  if txt == 'half':
    return str(28 // 2) + ' grams'
  elif txt == 'quarter':
    return str(28 // 4) + ' grams'
  elif txt == 'eighth':
    return str(round(28 / 8,2)) + ' grams'
  elif txt == 'sixteenth':
    return str(round(28 / 16,2)) + ' grams'
  else:
    return "invalid"

