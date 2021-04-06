
def is_prim_pyth_triple(l):
  
        def gcd(n1, n2):
                i = n1
                while i > 1:
                        if n1%i==0 and n2%i==0:
                                i  = 0
                                return False
                                break
                        else:
                                i-=1
                return True
                        
        l = sorted(l)
        return (l[0]**2 + l[1]**2 == l[2]**2) and gcd(l[0],l[1]) and gcd(l[0],l[2]) and gcd(l[1],l[2])

