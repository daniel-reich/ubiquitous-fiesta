
def million_in_month(first_month, multiplier):
  count = 1
  val = first_month
  
  while val <= 10**6:
    val += first_month * (multiplier ** count)
    count += 1
  return count

