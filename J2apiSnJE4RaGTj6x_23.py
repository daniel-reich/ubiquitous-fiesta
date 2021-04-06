
def find_broken_keys(txt1, txt2):
  
  broken_keys = []
  
  for n in range(len(txt1)):
    correct = txt1[n]
    unprov = txt2[n]
    
    if unprov != correct and correct not in broken_keys:
      broken_keys.append(correct)
  
  return list(broken_keys)

