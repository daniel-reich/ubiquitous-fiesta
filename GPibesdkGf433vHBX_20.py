
def goldbach_conjecture(n):
    L = [];
    if n % 2 == 1 and n > 2:
        return [];
    else:
        for O in range(n):
            for I in reversed(range(n)):
                if O+I == n and isPrime(O) and isPrime(I):
                    L.append(O);
                    L.append(I);
                    return L
  
def isPrime(X):
    if X<=1:
        return False
    C=0;
    n = 1;
    while n<X+1:
        if X % n ==0:         
            C+=1;
            n+=1;
        else:
            n+=1;
        if C>2:
            return False;
    return True;

