
def euclid_d2(cor1, cor2):
  if len(cor1)!=len(cor2): return(False)
  else: return(sum([(cor2[i]-cor1[i])**2 for i in range(len(cor1))]))
​
def check_orthg(cor1,cor2,cor3):
  distances=set([euclid_d2(cor1,cor2),euclid_d2(cor1,cor3),euclid_d2(cor2,cor3)])
  diag=max(distances)
  distances.remove(diag)
  if diag==sum(distances): return(True)
  else: return(False)
  
def is_rectangle(coordinates):
  if len(coordinates)!=4: return(False)
  coords=[eval(l) for l in coordinates]
  return(check_orthg(coords[0],coords[1],coords[2]) 
         and check_orthg(coords[0],coords[1],coords[3])  
         and check_orthg(coords[0],coords[2],coords[3]))

