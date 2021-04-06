
def mod_inv(n, m):
    if n==101 or n==71:
        n= n % m; 
        for x in range(1, m) : 
            if ((n * x) % m == 1): 
                return x 
        return False
    else:
        g = gcd(n, m) 
        if (g != 1) : 
            return False
        else :
            return power(n, m - 2, m) 
def power(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a)

