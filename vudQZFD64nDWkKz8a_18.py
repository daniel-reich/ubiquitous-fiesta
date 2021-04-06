
def grant_the_hint(txt):
  textList = txt.split()
  hint = ''
  hintList = []
  textLen = len(textList)
  hintLvl = 0
  while(hint != txt):
    for i in range(textLen):
      if(i!=0):
        hintList += ' '
      wordLen = len(textList[i])
      for j in range(wordLen):
        if(hintLvl > j):
          hint += '_'
        else:
          hint += textList[i][j]
    hintList.append(hint)
  hintList.append(txt)
  return hintList

