
def sexy_primes(b, n):
  
​
        def is_prime(n):
                a = n-1
                while a>1:
                        if n%a==0:
                                a = 0
                                return False
                                break
                        else:
                                a -= 1
                return True
​
              
        prime = [n for n in range(2,n) if is_prime(n)]
        if b == 2:
                return [(i,i+6) for i in prime if (i+6) in prime]
        else:
                return [(i,i+6,i+12) for i in prime if (i+6) in prime and (i+12) in prime]

