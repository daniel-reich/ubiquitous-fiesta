
def mark_maths(lst):
  print(lst) 
  total = len(lst)
  count = 0 
  for eqn in lst:
    equal_idx = eqn.index("=")
    for i in range(len(eqn)):
      if eqn[i] == "+":
        idx = i 
        if int(eqn[:idx]) + int(eqn[idx+1:equal_idx]) == int(eqn[equal_idx+1:]):
          count += 1 
      if eqn[i] == "-":
        idx = i 
        if idx < equal_idx:
          if int(eqn[:idx]) - int(eqn[idx+1:equal_idx]) == int(eqn[equal_idx+1:]):
            count += 1 
  return str(round((count/total) * 100)) + "%"

