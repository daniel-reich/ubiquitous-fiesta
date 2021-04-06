
def super_digit(n, k):
  if k==1 and int(n)<10: 
    return int(n)
  else:
    number = n*k
    digit_sum = sum(list(map(int, number[:])))
    return super_digit(str(digit_sum), 1)

