
def babbage(n):
    '''
    Returns the smallest positive integer whose square ends in n (or a special
    message if n is 269696).
    '''
    ans,n_str = 0, str(n)
    
    for i in range(int(n**0.5),n):
        if str(i*i).endswith(n_str):
            ans = i
            break
​
    if n == 269696:
        return 'Babbage was {}!'.format('correct' if ans == 99736 else 'incorrect')
​
    return ans

