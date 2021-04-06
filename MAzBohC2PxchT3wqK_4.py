
def shadow_sentence(a, b):
  test1 = lambda w1, w2: len(w1) == len(w2)
  test2 = lambda w1, w2: len([l8r for l8r in w1 if l8r in w2]) == 0
  
  a = a.split()
  b = b.split()
  
  if len(a) != len(b):
    return False
  
  for n in range(len(a)):
    aword = a[n]
    bword = b[n]
    
    t1 = test1(aword, bword)
    t2 = test2(aword, bword)
#print(t1, t2, aword, bword)
    if False in [t1, t2]:
      return False
  
  return True

