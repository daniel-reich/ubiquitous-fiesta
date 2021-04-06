
def sum_round(num):
  A=[str(num)[i]+'0'*(len(str(num))-i-1) for i in range(len(str(num)))]
  A=[x for x in A if not all(y=='0' for y in x)]
  return ' '.join(A[::-1])

