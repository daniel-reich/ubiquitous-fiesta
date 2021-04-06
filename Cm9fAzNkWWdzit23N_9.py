
def wave(txt):
  result = []
  for x in range(len(txt)):
    if txt[x] == " ":
      continue
    result.append(txt[:x].lower() + txt[x].upper() + txt[x + 1:].lower())
  return result

