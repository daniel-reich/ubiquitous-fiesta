
def diag_dom(arr):
  lst = []
  for x in range(len(arr)):
    lst.append(sum([abs(i) for i in arr[x]])-abs(arr[x][x])<abs(arr[x][x]))
  return all(lst)

