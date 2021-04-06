
def generate_rug(n, direction):
    '''
    Returns an n x n matrix withe the numbers 0 to n - 1 arranged diagonally
    as per direction, instructions above.
    '''
    numbers = [i for i in range(n-1,-1,-1)] + [i for i in range(1,n)]
    
    if direction == 'left':
        start = len(numbers) // 2  # start point for 1st row
        inc = -1   # direction of sliding window
        end = -1   # end of sliding window
    else:
        start = 0
        inc = 1
        end = n
​
    return [numbers[i : i + n] for i in range(start, end, inc)]

