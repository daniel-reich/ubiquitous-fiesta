
def is_prime(n):
    divisors = 0
    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            divisors += 1
    if divisors == 1:
        return True
    else:
        return False
​
def is_palindrome(n):
    n = str(n)
    n_rev = n[-1::-1]
    if n == n_rev:
        return True
    else:
        return False
​
def do_reverse(n):
    n = str(n)
    reverse = int(n[-1::-1])
    return reverse
    
    
def do_flipped(n):
    n1 = list(str(n))
    for i in range(len(n1)):
        if n1[i] == '6':
            n1[i] = '9'
        elif n1[i] == '9':
            n1[i] = '6'
    result = int(''.join(n1))
    return result
​
def bemirp(n):
  if(is_prime(n) and is_prime(do_reverse(n)) and is_prime(do_flipped(n)) and is_prime(do_reverse(do_flipped(n))) and (not is_palindrome(n))):
    return "B"
  elif(is_prime(n) and is_prime(do_reverse(n)) and (not is_palindrome(n))):
    return "E"
  elif(is_prime(n)):
    return "P"
  else:
    return "C"

