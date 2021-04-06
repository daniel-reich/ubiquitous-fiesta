
def construct_fence(p):
  return "H"*round((1000000/int(p.strip("$").replace(",",""))))

