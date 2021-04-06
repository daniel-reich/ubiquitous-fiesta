
def bacteria(final_mass):
  bac=[1]
  day=0
​
  while sum(bac)<final_mass:
    day+=1 #increase day
    bac=[x/2+1 for x in bac] #half mass plus 1
    bac=bac+bac # bacteria duplicated
    
  return day

