
def oddeven(lst):
  evens = [i for i in lst if i % 2 == 0]
  odds = [i for i in lst if i % 2 != 0]
  return len(odds) > len(evens)

