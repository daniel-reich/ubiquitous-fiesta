
import re
def can_pay_cost(m, c):
  A=(re.findall(r'(\d+)?([A-Z]+)?', c))[0]
  if A[0] and A[1]:
    if int(A[0])+len(A[1])<=len(m):
      for x in A[1]:
        if bool(re.search(x, m)):
          m=re.sub(x,'',m,1)
        else:
          return False
      return len(m)>=int(A[0])
    else:
      return False
  elif A[0] and not A[1]:
    return len(m)>=int(A[0])
  elif not A[0] and A[1]:
    for x in A[1]:
      if bool(re.search(x, m)):
        m=re.sub(x,'',m,1)
      else:
        return False
    return True
  else:
    return True

