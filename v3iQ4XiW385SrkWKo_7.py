
def final_result(lst):
  check = True
  while check and len(lst)>1:
    check = False
    for i in range(len(lst)-1):
      a = i
      for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
          b = j
          check = True
        else:
          break
      if check:
        del lst[a:b+1]
        break
  return lst

