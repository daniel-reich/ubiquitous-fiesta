
def number_len_sort(lst):
  A=[]
  for n in range(len(lst)):
    a = int(lst[n])
    if a < 10:
      A.append(a)
  for n in range(len(lst)):
    a = int(lst[n])
    if a < 100 and a >=10:
      A.append(a) 
  for n in range(len(lst)):
    a = int(lst[n])
    if a < 1000 and a >=100:
      A.append(a)       
  for n in range(len(lst)):
    a = int(lst[n])
    if a < 10000 and a >=1000:
      A.append(a) 
  return A

