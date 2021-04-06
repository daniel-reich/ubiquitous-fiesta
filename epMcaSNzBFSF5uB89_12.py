
def currently_winning(scores):
  even=0
  odd=0
  evenlst=[]
  oddlst=[]
  for i in range(len(scores)):
    if i%2==0:
      even=even+scores[i]
      evenlst.append(even)
    else:
      odd=odd+scores[i]
      oddlst.append(odd)
  lst3=[]
  for i in range(len(oddlst)):
    if evenlst[i]>oddlst[i]:
      lst3.append("Y")
    elif evenlst[i]==oddlst[i]:
      lst3.append('T')
    else:
      lst3.append('O')
  return lst3

