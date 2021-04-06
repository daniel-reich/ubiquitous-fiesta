
def final_result(lst):
    '''
    Combines contiguous blocks of the same character in lst repeatedly until
    no further combination occurs then returns the result as per instructions.
    '''
    while True:
        a = b = 0
        for i in range(len(lst) - 1):
            if lst[i] == lst[i+1]:
                a = i
                b = a + 1
                while b < len(lst) and lst[b] == lst[a]:
                    b += 1
                break
​
        if b == a: # no change
            return lst
        del lst[a:b]  # pop off 1st contiguous sequence

