
def major_sum(lst):
  pos = sum(i for i in lst if i>0)
  neg = sum(i for i in lst if i < 0)
  zeros = sum(1 for i in lst if i == 0)
  res = max(pos, abs(neg), zeros)
  return pos if res==pos else neg if res == abs(neg) else zeros

