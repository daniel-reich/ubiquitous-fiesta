
def sig_figs(num):
  if num == 0: 
    return 0
  numm = str(num)
  numm = numm.lstrip("-.0")
  
  if "." in numm:
    count = len(numm)-1
  elif "." in str(num): 
    count = len(numm)
  else: 
    numm = numm.rstrip("0")
    count = len(numm)
  return count

