
def trailing_zeros(n):
   # Initialize count
   count = 0
   # update Count
   i = 5
   while (n / i>= 1):
      count += int(n / i)
      i *= 5
   return int(count)

