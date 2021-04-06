
def wave(txt):
  result = []
  for x in range(len(txt)):
    if txt[x].isalpha():
      wave = txt[:x]+txt[x].upper()+txt[x+1:]
      result.append(wave)
    else:
      pass
  return result

