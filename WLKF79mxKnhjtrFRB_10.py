
def is_good_match(lst):
  ret = []
  if len(lst)%2 == 1:
    return 'bad match'
  for i in range(0,len(lst),2):
    ret.append(lst[i]+lst[i+1])
  return ret

