
def million_in_month(first_month, multiplier):
  months=1
  saved=first_month
  while True:
    first_month=first_month*multiplier
    saved+=first_month
    months+=1
    if saved>=1000000:return months

