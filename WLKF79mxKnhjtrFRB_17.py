
def is_good_match(lst):
  if len(lst)%2==1:
    return 'bad match'
  elif len(lst)%2==0:
    return [x+y for x,y in zip(lst[::2],lst[1::2])]

