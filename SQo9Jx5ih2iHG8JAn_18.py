
def expanded_form(n):
  n = str(n)
  k = [10**i for i in range(len(n)-1,-1,-1)]
  return ' + '.join([str(int(i)*j) for i,j in zip(n,k) if str(int(i)*j)!='0'])

