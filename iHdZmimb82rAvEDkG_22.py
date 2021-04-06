
def bitwise_index(lst):
    '''
    Returns a dictionary indicating the parity of the largest even integer in
    lst and the integer itself or an error message if there are none.
    '''
    biggest = float('-inf')
    idx = -1
    parity = ''
​
    for i, num in enumerate(lst):
        if num > biggest:
            if not num&1:  # even
                biggest = num
                idx = i
                parity = ('even', 'odd')[i&1]
​
    return {'@{} index {}'.format(parity,idx): biggest} if idx > -1 else \
           'No even integer found!'

