
def leader(lst):
  greaterList = []
  length = len(lst)
  for i in range(length):
    for j in range(i+1,length):
      if lst[i] <= lst[j]:
        break
    else:
      greaterList.append(lst[i])
  return greaterList

