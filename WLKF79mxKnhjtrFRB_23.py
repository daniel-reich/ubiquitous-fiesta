
def is_good_match(lst):
  if len(lst)%2: return 'bad match'
  return [lst[x] + lst[x+1] for x in range(0, len(lst), 2)]

