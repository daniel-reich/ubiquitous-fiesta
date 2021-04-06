
def oddeven(lst):
  ood = [i for i in lst if i % 2 != 0]
  evens = [i for i in lst if i % 2 == 0]
  
  return len(ood) > len(evens)

