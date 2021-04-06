
def is_good_match(lst):
  return [lst[x] + lst[x + 1] for x in range(0, len(lst), 2)] if len(lst) % 2 == 0 else 'bad match'

