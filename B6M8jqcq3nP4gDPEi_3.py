
def iso_group(lst):
    '''
    Uses a recursive approach to return the maximum value(s) in lst as per
    the instructions
    '''
​
    def _iso_group(lst, biggest):
        '''
        Helper to iso_group - updates list biggest to that it contains
        the maximum value(s) in lst
        '''
        if len(lst) > 0:
            num = lst[0]
            if num > biggest[0]:
                 biggest = [num]
            elif num == biggest[0]:
                biggest.append(num)
            biggest = _iso_group(lst[1:], biggest)
​
        return biggest
​
    biggest = _iso_group(lst[1:], [lst[0]])
    return biggest if len(biggest) > 1 else biggest[0]

