
def divisible_by_left(n):
  newlist = []
  first = str(n)
  for x in first:
    newlist += [int(x)]
  
  final = []
  length = len(newlist)
  while length > 0:
    if length == 1:
      final = [False] + final
      return final
    elif newlist[length-2] == 0:
      final = [False] + final
      length = length - 1
    elif newlist[length-1] % newlist[length-2] == 0:
      final = [True] + final
      length = length - 1
    else:
      final = [False] + final
      length = length - 1

