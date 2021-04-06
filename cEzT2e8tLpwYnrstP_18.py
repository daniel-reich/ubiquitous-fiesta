
def swap_d(k, v, swapped):
  thisdict = {
  
  }
  for a in range(len(k)):
    if not swapped:
      thisdict[k[a-1]] = v[a-1]
    else:
      thisdict[v[a-1]] = k[a-1]
  return thisdict
print (swap_d(["one","two","three"],["1","2","3"],False))

