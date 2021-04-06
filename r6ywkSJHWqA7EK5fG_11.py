
def printgrid(rows, cols):
  it = 1
  lst = [0]*cols
  for i in range(len(lst)):
    temp = []
    for j in range(rows):
      temp.append(it)
      it+=1
    lst[i]=temp[::-1]
  return [[i[j] for i in lst] for j in range(len(lst[0]))][::-1]

