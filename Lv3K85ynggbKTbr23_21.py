
def float_sum(A, B):
  strA,strB=str(A),str(B)
  try:
    fracDigALen=len(strA)-1-strA.index('.')
  except ValueError: fracDigALen=0
  try:
    fracDigBLen=len(strB)-1-strB.index('.')
  except ValueError: fracDigBLen=0
  mxfracDigLen=fracDigALen
  if fracDigALen>fracDigBLen:
    strB=strB+'0'*(fracDigALen-fracDigBLen)    
  elif fracDigBLen>fracDigALen:
    strA=strA+'0'*(fracDigBLen-fracDigALen)
    mxfracDigLen=fracDigBLen
  strA=strA.replace('.','')
  strB=strB.replace('.','')
  strRes=str(int(strA)+int(strB))
  return float(strRes[:-mxfracDigLen]+'.'+strRes[-mxfracDigLen:])

