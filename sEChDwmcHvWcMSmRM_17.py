
def find_the_falsehoods(lst):
  nlst=[]
  for x in range(len(lst)):
    if bool(lst[x]) == False:
      nlst.append(lst[x])
  return nlst

