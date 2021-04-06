
def is_prime(num):
  return False if num == 1 \
    else not sum( [ 1 for d in range(2,num) if not num%d  ] )

