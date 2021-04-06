
def worded_math(equ):
  equ = equ.lower()
  inNum = {'zero':'0','one':'1','two':'2','plus':'+','minus':'-'}
  outNum = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four'}
  return outNum[eval(''.join(inNum[x] for x in equ.split()))]

