
def bird_code(lst):
  result=[]
  for names in lst:
    names=names.replace("-"," ")
    words=names.count(" ")+1
    wordsArr=names.split(" ")
    if words==1:
      result.append(wordsArr[0][0:4].upper())
    elif words==2:
      result.append(wordsArr[0][0:2].upper()+wordsArr[1][0:2].upper())
    elif words==3:
      result.append(wordsArr[0][0:1].upper()+wordsArr[1][0:1].upper()+wordsArr[2][0:2].upper())
    elif words==4:
      result.append(wordsArr[0][0:1].upper()+wordsArr[1][0:1].upper()+wordsArr[2][0:1].upper()+wordsArr[3][0:1].upper())
  return result

