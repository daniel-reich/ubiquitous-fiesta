
def check(lst):
  return ('NO', 'YES')[any(lst[i:] + lst[:i] == sorted(lst) for i in range(1, len(lst)))]

