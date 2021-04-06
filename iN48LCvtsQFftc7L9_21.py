
def word_search(letters, words):
  horizontal, vertical = [letters[x:x+8] for x in range(0,64,8)], ["".join([letters[x] for x in range(y,64,8)]) for y in range(8)]
  diagonal = []
  for i in range(8):
    temp, temp2, temp3, temp4 = "", "", "", ""
    for j in range(8):
      if i +j <= 7:
        temp += horizontal[j][j+i]
      if j - i >= 0:
        temp2 += horizontal[j][j-i]
      if 7-(i +j) >= 0:
        temp3 += horizontal[j][abs(7-(j+i))]
      if 7-(j - i) <= 7:
        temp4 += horizontal[j][abs(7-(j-i))]
    if temp3 not in diagonal: diagonal.append(temp3)
    if temp4 not in diagonal: diagonal.append(temp4)
    if temp2 not in diagonal: diagonal.append(temp2)
    if temp not in diagonal: diagonal.append(temp)
  while len(words) > 0:
    start = len(words)
    for i in horizontal+vertical+diagonal:
      if words[-1].upper() in i or words[-1].upper() in i[::-1]:
        words.pop()
        break
    if len(words) == start: return False
  return True

