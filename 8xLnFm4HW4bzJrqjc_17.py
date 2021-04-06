
def digit_distance(num1, num2):
  count = 0 
  while num1 > 0:
    count += abs(num1%10-num2%10)
    num1 //= 10
    num2 //= 10
  return count

