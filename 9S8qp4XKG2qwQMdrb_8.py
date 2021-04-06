
def ways_to_climb(n):
        if n == 0:
            return 1 
        if n ==1 :
            return 1 
        if n ==2 :
            return 2 
        if n == 3:
            return 3 
        
        d = {1:1,2:2}
        for i in range(3,n+1):
            k = d[i-2] + d[i-1]
            d[i] = k
            
        return d[n]

