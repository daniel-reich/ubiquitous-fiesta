
def is_good_match(lst):
  if len(lst) % 2 != 0:
    return "bad match"
  lst1 = [x for x in lst[0::2]]
  lst2 = [x for x in lst[1::2]]
  return [x + y for x,y in zip(lst1, lst2)]

