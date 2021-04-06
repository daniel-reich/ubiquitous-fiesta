
def expanded_form(num):
  s=str(num)[::-1]
  A=[x+'0'*i for i, x in enumerate(s) if x!='0'][::-1]
  return ' + '.join(A)

