
def lambda_depth(num):
  c = [0, num]
  def g ():
    c[0] +=1
    if c[0] == c[1]:
      return "edabit"
    else:
      return g
        
  if num == 0:
    return "edabit"
  return g

