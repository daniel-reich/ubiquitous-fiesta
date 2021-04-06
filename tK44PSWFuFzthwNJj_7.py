
def club_entry(word):
  alpha="abcdefghijklmnopqrstuvwxyz"
  str = word
  list1=[] 
  list1[:0]=str
  print(len(list1))
  for index,i in enumerate(list1):
    if (index)< len(list1)-1:
      if i==list1[index+1]:
        print("character is: ",i,"index is: ",index+2)
        alphaPosition = alpha.index(i)+1
  return alphaPosition*4

