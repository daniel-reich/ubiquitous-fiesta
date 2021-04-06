
def reversible_inclusive_list(start, end):
  # recursive solution here
  if start==end:
    return [start]
  elif start<end:
    return reversible_inclusive_list(start, end-1)+[end]
  else:
    return reversible_inclusive_list(start, end+1)+[end]

