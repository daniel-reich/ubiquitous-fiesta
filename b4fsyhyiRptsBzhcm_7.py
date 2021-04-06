
def sum_even_nums_in_range(start, stop):
    result = 0
    if not (start%2==0):
        start+=1
    for i in range(start, stop+1, 2):      
        result += i
    return result

