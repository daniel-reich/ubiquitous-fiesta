
def delete_occurrences(mylist, num):
  from collections import Counter 
  mylist = list(reversed(mylist))
  counter_list = Counter(mylist)
  for variables in counter_list:
    if counter_list[variables] >= num: 
      for i in range(0, counter_list[variables]-num):
        del(mylist[mylist.index(variables)])
  return list(reversed(mylist))

