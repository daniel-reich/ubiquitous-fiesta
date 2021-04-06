
def worded_math(equ):
  num = {'zero':'0', 'one':'1', 'two':'2', 'plus':'+', 'minus':'-', 0:'Zero', 1:'One', 2:'Two'}
  return num[eval(''.join([v for i in equ.lower().split() for k,v in num.items() if i == k]))]

