
def even_last(lst):
  try:
    evens = lst[::2]
    last = lst[-1]
    return sum(number * last for number in evens)
  except IndexError:
    return 0

