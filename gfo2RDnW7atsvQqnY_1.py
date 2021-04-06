
def count_smileys(lst):
  res=0
  for i in lst:
    if(i[0] in ":;" and i[-1] in ")D"):
      if(len(i)==3 and i[1] in "-~"):
        res+=1
      elif(len(i)==2):
        res+=1
  return(res)

