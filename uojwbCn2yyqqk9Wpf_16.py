
def is_untouchable(n):
    if n < 2:
        return 'Invalid Input'
    
    limit = n**2
    totals = [1 for _ in range(limit)]
    
    for i in range(2, limit):
        j = i
        while j < limit - 1:
            totals[j] += i
            j += i       
    touchable = [i for i in range(2, limit) if totals[i] - i == n]
    return True if not touchable else touchable

