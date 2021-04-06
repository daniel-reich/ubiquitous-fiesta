
def equal(a, b, c):
  lst = [a,b,c]
  answer = max([ lst.count(x) for x in [a,b,c] ])
  return answer if answer != 1 else 0

