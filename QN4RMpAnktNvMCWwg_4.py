
def id_mtrx(n):
  i=0
  j=0
  if type(n) != int:
    return 'Error'
  elif n >=0:
    return [[1 if i == j else 0 for i in range(n)]for j in range(n)]
  elif n < 0:
    return [[1 if i == j else 0 for i in range(abs(n))]for j in range(abs(n))][::-1]

