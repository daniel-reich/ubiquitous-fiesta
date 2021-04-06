
def ping_pong(lst, win):
  lst2=[]
  for i in range(len(lst)):
   lst2.append(lst[i])
   lst2.append("Pong!")
  if win==True: return lst2
  else : 
   lst2.pop(-1)
   return lst2

