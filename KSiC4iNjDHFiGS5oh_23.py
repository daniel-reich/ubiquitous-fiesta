
def is_super_d(n):
  resoult = "".join(["Super-{} Number".format(x) for x in range(2, 10) if str(x)*x in str(x*n**x)]) 
  if resoult:
    return resoult
  else:
    return "Normal Number"

