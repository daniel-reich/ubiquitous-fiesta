
def is_good_match(lst):
  return [i+j for i,j in zip(lst[::2],lst[1::2])] if len(lst)%2==0 else 'bad match'

