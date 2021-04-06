
def wave(txt):
  if txt in " ": return []
  result = []
  for i in range(len(txt)):
    txt2 = txt[0:i] + txt[i].upper()+txt[i+1:]
    if not txt2.islower():
      result.append(txt2)
  return result

