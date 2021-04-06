
def largest_gap(lst):
  return [lst.sort(), max([lst[i+1]-lst[i] for i in range(len(lst)-1)])][1]

