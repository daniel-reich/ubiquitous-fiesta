
def get_discounts(nums, d):
  f=d.strip("%")
  d_int=int(f)
  final=[]
  for x in nums:
    k=(x*d_int)/100
    s=str(k)
    if ".0" in s:
      u=float(s)
      final.append(int(u))
      
    elif ".5" or ".2" in s:
      u=s.format(":1f")
      final.append(float(u))
  return final

