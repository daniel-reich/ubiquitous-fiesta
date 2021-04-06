
def number_of_repeats(s):
  mylist = []
  for i in s:
    mylist.append(s.count(i))
  return min(mylist)

