
def id_mtrx(n):
  if not isinstance(n,int):
    return 'Error'
  mtx = [[1 if i==j else 0 for j in range(abs(n))] for i in range(abs(n))]
  if n < 0:
    mtx = [row[::-1] for row in mtx]
  return mtx

