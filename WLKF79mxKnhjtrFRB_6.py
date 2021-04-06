
def is_good_match(lst):
  return 'bad match' if len(lst)%2 else [a+b for a, b in zip(lst[::2], lst[1::2])]

