
def balanced(lst):
  first = lst[:len(lst)//2]
  second = lst[len(lst)//2:]
  return lst if sum(first) == sum(second) else first + first if sum(first) > sum(second) else second + second

