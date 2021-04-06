
def find_odd(lst):
  liste1 = set(lst)
  for i in liste1 :
    if lst.count(i)%2 != 0 :
      return i
    else : pass

