
def pluralize(lst):
  tab = []
  for i in lst :
     if  lst.count(i )==1:
         tab.append(i)
     elif lst.count(i) >1 :
         tab.append(i+"s")
  val=[]                
  for j in tab :
      if j not in val:
        val.append(j)
  return set(val)

