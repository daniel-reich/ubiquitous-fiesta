
def to_boolean_list(word):
  lst1=[]
  lst2=[]
  for i in word:
      if (ord(i)-64)%2==0:
          lst1.append(0)
      else:
          lst1.append(1)
  for i in lst1:
      if i==1:
          lst2.append(True)
      else:
          lst2.append(False)
  return lst2

