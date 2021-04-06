
def risiko(attacker, defender):
 # sort lists
 att=list(reversed(sorted(attacker)))
 defe=list(reversed(sorted(defender)))
 #print(att,defe)
 # while not end of list of either
 i=0
 count=0
 while i < len(att) and i < len(defe):
  # compare i
  if defe[i] < att[i]:
   count+=1
  i+=1
 return count

