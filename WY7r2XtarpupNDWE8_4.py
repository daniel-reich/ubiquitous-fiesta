
def tower_of_hanoi(n, move):
    disks = [list(range(n, 0, -1)), [], []]
    c = []
    def helper(n, source, target, spare):
        
        if n == 1:
            
            disks[target].append(disks[source].pop())    
​
            c.append([x[:] for x in disks])
            return 
                
        
        helper(n-1, source, spare, target)
        helper(1, source, target, spare)
        helper(n-1, spare, target, source)
​
    helper(n, 0, 2, 1)
    return tuple(c[move-1])

