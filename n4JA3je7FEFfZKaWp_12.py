
def million_in_month(first_month, multiplier):
  count = 1
  total = first_month
  while total<1000000:
    first_month*=multiplier
    total+=first_month
    count+=1
  return count

