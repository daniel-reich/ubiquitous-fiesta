
def matrix_mult(m1, m2):
  i = 0
  j = 1
  a1 = m1[i][i]
  a2 = m1[i][j]
  a3 = m1[j][i]
  a4 = m1[j][j]
​
  b1 = m2[i][i]
  b2 = m2[i][j]
  b3 = m2[j][i]
  b4 = m2[j][j]
​
  return [[a1*b1 + a2*b3, a1*b2 + a2 * b4],
  [a3*b1 + a4*b3, a3*b2 + a4*b4]]

