
def largest_even(lst):
    max = -1
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if max == -1:
                max = lst[i]
            elif max < lst[i]:
                max = lst[i]
            
    return max

