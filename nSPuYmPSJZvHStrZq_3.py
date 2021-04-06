
def oddeven(lst):
  odds = [i for i in lst if i % 2]
  evens = [i for i in lst if not i % 2]
  return len(odds) > len(evens)

