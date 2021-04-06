
def isbn13(isbn):
    '''
    Processes the input isbn as per the instructions
    '''
    CHK_10 = list(range(10,0,-1))
    CHK_13 = '13'*6 + '1'
    ok = lambda x,y,z: sum(int(y[i]) * (int(d) if d.isnumeric() else 10)
                                   for i, d in enumerate(x)) % z == 0
    
    if len(isbn) == 13:
        if ok(isbn, CHK_13, 10):
            return 'Valid'
        return 'Invalid'
    
    if len(isbn) == 10:
        if not ok(isbn, CHK_10, 11):
            return 'Invalid'
        
        if isbn[-1] == 'X':
            isbn = isbn[:-1] + '0'
            
        isbn = '978' + isbn[:-1] + str((int(isbn[-1]) + 1)%10)
        while not ok(isbn, CHK_13, 10):
            isbn = isbn[:-1] + str((int(isbn[-1]) + 1)%10)
        return isbn
​
    return 'Invalid'

