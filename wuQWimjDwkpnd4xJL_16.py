
def balanced(lst):
  return lst[len(lst) // 2:] * 2 if sum(lst[len(lst) // 2:]) > sum(lst[:len(lst) // 2]) else \
    lst[:len(lst) // 2] * 2 if sum(lst[len(lst) // 2:]) < sum(lst[:len(lst) // 2]) else lst

