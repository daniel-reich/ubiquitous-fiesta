
def numbers_to_ranges(lst):
  if not lst:
    return []
  else:
    if len(lst)==1:
      return [str(lst[0])]
    else:
      A=[]
      for i in range(len(lst)-1):
        if lst[i+1]-lst[i]!=1:
          A.append(lst[i])
          A.append(lst[i+1])
      if not A:
        return [str(lst[0])+'-'+str(lst[-1])]
      else:
        if lst[0]==A[0]:
          return [str(lst[0]), str(A[-1])+'-'+str(lst[-1])]
        return [str(lst[0])+'-'+str(A[0]), str(A[-1])+'-'+str(lst[-1])]

