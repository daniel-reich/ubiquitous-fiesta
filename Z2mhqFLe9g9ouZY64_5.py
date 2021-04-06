
def is_valid_subsequence(lst, seq):
​
  #Get rid of obvious failures first:
​
  for l8r in seq:
    if l8r not in lst or lst.count(l8r) < seq.count(l8r):
      return False
  
  #Then find obvious winners:
​
  if seq in lst:
    return True
​
  # To find the rest, get rid of all extraneous numbers in lst!!
​
  nl = [i for i in lst if i in seq]
​
  return seq in nl or seq == nl

