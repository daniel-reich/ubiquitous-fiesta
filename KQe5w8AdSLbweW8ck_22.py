
def char_at_pos(r, s):
  solutionOdd = []
  solutionEven = []
  if s == "odd":
    for i in range(0,len(r),2):
      solutionOdd.append(r[i])
    if type(r) == str: 
      return "".join(solutionOdd)
    else:
      return solutionOdd
  else: 
    for i in range(1,len(r),2):
      solutionEven.append(r[i])
    if type(r) == str: 
      return "".join(solutionEven)
    else:
      return solutionEven

