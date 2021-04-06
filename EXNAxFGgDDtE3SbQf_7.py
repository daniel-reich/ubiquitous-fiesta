
def shuffle_count(n):
    
    def helper(l, ml, counter):
        l1 = ml[0:n//2]
        l2 = ml[n//2:]
        final = [j for i in zip(l1,l2) for j in i]
        counter += 1
        if final == l:
            return counter
        else:
            return helper(l, final, counter)
​
    l = list(range(1, n+1))
    return helper(l, l, 0)

