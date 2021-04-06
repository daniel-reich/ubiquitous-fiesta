
def is_narcissistic(n):
  digits = [int(i) for i in str(n)]
  multiple_digits = [i**len(str(n)) for i in digits]
  
  return sum(multiple_digits) == n

