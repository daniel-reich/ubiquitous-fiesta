
def is_untouchable(n):
    '''
    Returns True if n is not equal to the sum of the proper divisors of integers
    in the range 2 to n^2, otherwise a list of the numbers in that range whose
    sum matches it. n validated to be > 1
    '''
    if n < 2:
        return 'Invalid Input'
    
    def divisors(n):
        '''
        Returns the sum of the divisors of n
        '''
        divs = {1}
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                divs.add(i)
                divs.add(n // i)
​
        return sum(divs)
        
​
    total = [i for i in range(2, n * n + 1) if divisors(i) == n]
    return True if not total else total

