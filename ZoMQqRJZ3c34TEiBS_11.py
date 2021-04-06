
def playfair(txt, keyword):
  keyword, key = [], keyword
  for i in key: 
    if not i in keyword:
      keyword.append(i)
  keyword = "".join(keyword)
  cipher = [x.upper() for x in keyword] + [chr(x) for x in range(65,91) if chr(x) not in (keyword.upper())+"J" ]
  cipher = [cipher[x:x+5] for x in range(0,25,5)]
  if " " in txt: 
    txt = "".join([x.upper() for x in txt if x.isalnum()])
    while True:
      start = len(txt)
      txt = [txt[x:x+2] for x in range(0, len(txt), 2)]
      for i in range(len(txt)):
        if len(txt[i]) == 1: break
        if txt[i][0] == txt[i][1]:
          txt[i] = txt[i][0]+"X"+txt[i][1]
          break
      txt = "".join(txt)
      if len(txt) == start: break
    if len(txt) % 2 == 1: txt += "X"
    result = ""
    for i in [txt[x:x+2] for x in range(0, len(txt), 2)]:
      for j in range(len(cipher)):
        if i[0] in cipher[j]: left = [cipher[j].index(i[0]), j]
        if i[1] in cipher[j]: right = [cipher[j].index(i[1]), j]
      if left[1] == right[1]: result += cipher[left[1]][(left[0]+1)%5] + cipher[right[1]][(right[0]+1)%5]
      elif left[0] == right[0]: result += cipher[(left[1]+1)%5][(left[0])] + cipher[(right[1]+1)%5][right[0]]
      else: result += cipher[(left[1])][right[0]] + cipher[(right[1])][(left[0])]
  else: 
    result = ""
    for i in [txt[x:x+2] for x in range(0, len(txt), 2)]:
      for j in range(len(cipher)):
        if i[0] in cipher[j]: left = [cipher[j].index(i[0]), j]
        if i[1] in cipher[j]: right = [cipher[j].index(i[1]), j]
      if left[1] == right[1]: result += cipher[left[1]][(left[0]-1)] + cipher[right[1]][(right[0]-1)]
      elif left[0] == right[0]: result += cipher[(left[1]-1)][(left[0])] + cipher[(right[1]-1)][right[0]]
      else: result += cipher[(left[1])][right[0]] + cipher[(right[1])][(left[0])]
  return result

