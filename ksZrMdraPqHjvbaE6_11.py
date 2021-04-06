
def largest_even(lst):
    c =[i for i in lst if i%2 ==0]
    
    
    b = sorted(c,reverse = True)
    if c == []:
        return -1
    else:
        return b[0]

