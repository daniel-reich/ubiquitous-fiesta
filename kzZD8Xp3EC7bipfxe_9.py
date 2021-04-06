
def worded_math(equ):
  num = {'one':1,'zero':0}
  sign = {'plus':'+','minus':'-'}
  ans = {0:'Zero',1:'One',2:'Two'}
  a,op,b = equ.split()
  return ans[eval(str(num[a.lower()])+sign[op.lower()]+str(num[b.lower()]))]

