
def odd_sort(lst):
  evenindexes = list([x for x in range(len(lst)) if lst[x] % 2 == 0])
  evennumbers = list([x for x in lst if x % 2 == 0])
  newlist = []
  while len(newlist) != len(lst):
    newlist.append('')
  oddindexes = list([x for x in range(len(lst)) if lst[x] % 2 != 0])
  oddnumbers = sorted(list([x for x in lst if x % 2 != 0]))
  increment = 0
  for eachnumber in evenindexes:
    newlist[eachnumber] = evennumbers[increment]
    increment += 1
  increment = 0
  for eachnumber in oddindexes:
    newlist[eachnumber] = oddnumbers[increment]
    increment += 1
  return newlist

