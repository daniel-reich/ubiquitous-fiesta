
def box_seq(step):
  ans = 0
  for i in range(1,step+1):
    if i%2 == 1:
      ans += 3
    else:
      ans -= 1
  return ans

