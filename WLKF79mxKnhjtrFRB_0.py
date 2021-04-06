
def is_good_match(lst):
  return 'bad match' if len(lst) % 2 else [sum(lst[i:i+2]) for i in range(0, len(lst), 2)]

