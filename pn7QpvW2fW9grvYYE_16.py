
def find_fulcrum(lst):
  num = [n for n in lst if sum(lst[:lst.index(n):]) == sum(lst[lst.index(n)+1::]) ]
  if num == []:
    return -1
  return num[0]

