
def block(lst):
    return sum([len(lst)-(i+1)  for i in range(len(lst)) for j in lst[i]  if j==2])

