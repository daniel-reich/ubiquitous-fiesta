
def to_boolean_list(word):
  A=[]
  for x in word:
    if (ord(x)-ord('a')+1)%2:
      A.append(True)
    else:
      A.append(False)
  return A

