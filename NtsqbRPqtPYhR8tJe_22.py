
def blocks(step):
  if step == 0:
    return 0
  return 0.5*step**2 + 5.5*step -1
​
# an**2 +bn + c
# 2a = second difference
# 3a + b = second term - first term
# a + b + c = first term
# sequence = 5,12,20,29,39
# 3a + b = 7
#
# first difference = 7,8,9,10
# second diff = 1 = 2a: a = 0.5
# 3a + b = 7 : 1.5 + b = 7 ....b=5.5
# c = 5 - 5.5 -0.5 = -1

