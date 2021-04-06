
def steps_to_convert(txt):
  upCnt=0
  for x in txt:
    if x.isupper(): upCnt+=1
  return upCnt if 2*upCnt<len(txt) else len(txt)-upCnt

