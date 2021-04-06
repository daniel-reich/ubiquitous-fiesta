
def expanded_form(num):
  A=str(num).split('.')
  B=[x+'0'*i for i, x in enumerate(A[0][::-1]) if x!='0'][::-1]
  C=[x+'/'+'1'+'0'*(i+1) for i, x in enumerate(A[1]) if x!='0']
  return ' + '.join(B+C)

