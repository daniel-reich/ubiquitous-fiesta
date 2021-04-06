
def add_two_numbers(l1, l2):
    nbr1 = sum([dig * 10**ix
            for ix, dig in enumerate(l1.get_data())])
    nbr2 = sum([dig * 10**ix
            for ix, dig in enumerate(l2.get_data())])
    str1 = [int(s) for s in str(nbr1 + nbr2)] 
    str1.reverse() 
    lt3 = ListNode( str1[0])
    str1.pop(0)
    lt3.add_data(str1)
    return lt3

