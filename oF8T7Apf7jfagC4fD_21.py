
def antipodes_average(lst):
  result = []
  if len(lst)>1:
    for i in range(len(lst)//2):
      result.append((lst[i] +lst[-(i+1)])/2)
    return result

