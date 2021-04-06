
def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total
​
def calc(s):
  n1 = ''.join(str(ord(i)) for i in s)
  n2 = n1.replace('7', '1')
  
  return sum_digits(int(n1)) - sum_digits(int(n2))

