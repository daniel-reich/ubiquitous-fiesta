
def float_sum(A, B):
  return round(A + B, max(len(str(A).split('.')[-1]),len(str(B).split('.')[-1])))

