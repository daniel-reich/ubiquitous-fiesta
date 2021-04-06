
def return_unique(lst):
  a = [i for i in lst if lst.count(i)<2]
  return a

