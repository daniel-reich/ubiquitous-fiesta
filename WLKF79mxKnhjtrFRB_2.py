
def is_good_match(lst):
  if len(lst) % 2:
    return 'bad match'
  return [a+b for a, b in zip(lst[::2], lst[1::2])]

