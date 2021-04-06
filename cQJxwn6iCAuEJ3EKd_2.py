
def digits_count(n):
  return 1 if -10<n<10 else 1+digits_count(n//10)

