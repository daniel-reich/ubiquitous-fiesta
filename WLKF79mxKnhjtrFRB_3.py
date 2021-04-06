
def is_good_match(lst):
  return "bad match" if len(lst)%2==1 else [x+y for x,y in zip(lst[::2],lst[1::2])]

