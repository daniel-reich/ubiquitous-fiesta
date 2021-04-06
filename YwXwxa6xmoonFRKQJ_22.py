
def josephus(n):
​
    def find_left(n, l):
                 
        for i in range(1, len(l)):
            j = (n+i)%len(l)
            if l[j] == 'a':
                return j
​
​
    if n < 2:
        return False
    else:
​
        ind = 0
        ind_n = -1
        arr = ['a' for z in range(n)]   
        
        while arr.count('a') > 1:
        
            ind = find_left(ind_n, arr)            
            ind_n = find_left(ind, arr)
            arr[ind_n] = 'x'
      
        return ind

