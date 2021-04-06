
def sum_neg(lst):
  positive=[num for num in lst if num>0]
  negative=[num for num in lst if num<0]
  if lst==[]: return []
  return [len(positive), sum(negative)]

