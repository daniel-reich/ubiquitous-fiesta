
def number_pairs(txt):
  txt=txt.split(" ")
  temp=[]
  count=0
  for i in range(1,len(txt)):
    c=0
    if txt[i] not in temp:
      for j in range(i,len(txt)):
        if txt[i]==txt[j]:
          c+=1
      count+=c//2
      temp.append(txt[i])
  return count

