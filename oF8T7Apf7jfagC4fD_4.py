
def antipodes_average(lst):
  total = 0
  newlist = []
  newlist2 = []
  if len(lst) % 2 != 0:
    middle = len(lst) // 2
    second_half = lst[middle+1:][::-1]
    first_half = lst[:middle]
    for i in range(len(first_half)):
      total = first_half[i] + second_half[i]
      newlist.append(total)
    for eachnumber in newlist:
      newnumber = eachnumber / 2
      if '.0' in str(newnumber):
        newlist2.append(int(newnumber))
      else:
        newlist2.append(newnumber)
    return newlist2
  else:
    middle = len(lst) // 2
    right_part = lst[middle:][::-1]
    left_part = lst[:middle]
    for i in range(len(left_part)):
      total = left_part[i] + right_part[i]
      newlist.append(total)
    for eachnumber in newlist:
      newnumber = eachnumber / 2
      newlist2.append(newnumber)
    return newlist2

