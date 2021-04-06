
def is_good_match(lst):
  if len(lst)%2:
    return 'bad match'
  return [sum(lst[i:i+2]) for i in range(0,len(lst),2)]

