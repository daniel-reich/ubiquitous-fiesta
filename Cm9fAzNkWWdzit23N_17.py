
def wave(txt):
  cnt = 0
  newAry = []
  while cnt < len(txt):
    if txt[cnt] is not " ":
      newAry.append(txt[0:cnt] + txt[cnt].upper() + txt[cnt + 1:len(txt)])
      cnt += 1
    else:
      cnt += 1
  return(newAry)

