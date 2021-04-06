
def divisible(arg, S=0):
​
  if S == 0 and arg == 1:
    S = 1
  elif S == 0 and arg == 0:
    S = 0
  elif S == 1 and arg == 0:
    S = 2
  elif S == 1 and arg == 1:
    S = 0
  elif S == 2 and arg == 0:
    S = 1
  elif S == 2 and arg == 1:
    S = 2
​
  def helper(p):
    return divisible(p, S)
    
  if arg == "state":
    return "S{0}".format(S)
  elif arg == "stop":
    if S == 0:
      return "accept"
    else : return "reject"
  else : return helper

