
def cutting_grass(lst, *cuts):
  result = []
  for i, n in enumerate(cuts):
    lst = [x-n for x in lst]
    if(0 in lst):
      result += (["Done"]*(len(cuts)-i))
      break
    else:
      result.append(lst)
  return result

