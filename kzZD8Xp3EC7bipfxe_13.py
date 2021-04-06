
def worded_math(equ):
  d={'zero':'0','one':'1','two':'2','plus':'+','minus':'-'}
  ls=['Zero','One','Two']
  for i in d:
    equ = equ.lower().replace(i,d[i])
  return ls[eval(equ)]

