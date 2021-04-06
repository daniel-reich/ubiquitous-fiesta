
def divisible(arg, current_state = "S0", end_state = "S0"): 
  def helper(p):
    return divisible(p, current_state, end_state)
  if current_state == "S0":
    if arg == 1:
      current_state = "S1"
  elif current_state == "S1":
    if arg == 1:
      current_state = "S0"
    elif arg == 0:
      current_state = "S2"
  elif current_state == "S2":
    if arg == 0:
      current_state = "S1"
      
      
  if arg == "stop":
    return "accept" if current_state == end_state else "reject"
  elif arg == "state":
    return current_state
    
  return helper

