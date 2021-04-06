
def return_unique(lst):
  d = [i for i in lst if lst.count(i)<2]
  return d

