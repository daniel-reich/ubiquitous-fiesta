
def trailing_zeros(n):
  # https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
    # Initialize result
    count = 0
 
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count

