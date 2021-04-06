
def f(A, c):
  aa = 1
  bb = -1*c**2
  cc = (2*A)**2
  
  dd = bb**2-4*aa*cc
  if dd < 0:
    return 'Does not exist'
​
  w1 = (-bb+(dd)**.5)/2
  w2 = (-bb-(dd)**.5)/2
​
  z1 = round(w1**.5,3)
  z2 = round(w2**.5,3)
  myans = [z1,z2]
  return sorted(myans)

