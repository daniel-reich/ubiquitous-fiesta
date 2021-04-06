
def is_good_match(lst):
  even = [v for i, v in enumerate(lst) if i % 2 == 0]
  odd = [v for i, v in enumerate(lst) if i % 2 != 0]
  return "bad match" if len(lst)%2 != 0 else [even[i] + odd[i] for i in range(len(even))]

