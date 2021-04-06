
def calculate_score(g):
 s=0
 for a,b in g:
  if a!=b:s+=2*(a+b in"PRRSSP")-1
 return[["Tie","Benson"][s<0],"Abigail"][s>0]

