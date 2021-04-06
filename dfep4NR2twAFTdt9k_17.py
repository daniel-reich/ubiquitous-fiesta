
def matrix_mult(m1, m2):
  a=m1[0][0]
  b=m1[0][1]
  c=m1[1][0]
  d=m1[1][1]
  e=m2[0][0]
  f=m2[0][1]
  g=m2[1][0]
  h=m2[1][1]
  top_left=(a*e)+(b*g)
  top_right=(a*f)+(b*h)
  bottom_left=(c*e)+(d*g)
  bottom_right=(c*f)+(d*h)
  return [[top_left,top_right],[bottom_left,bottom_right]]

