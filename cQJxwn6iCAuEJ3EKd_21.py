
def digits_count(num):
  # your recursive implementation 
  # of the code here
  return 1+digits_count(num//10) if abs(num)>10 else 1

