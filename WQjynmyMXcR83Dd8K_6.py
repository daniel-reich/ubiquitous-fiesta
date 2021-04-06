
def number_of_swaps(lst):
    swaps = 0
​
    while lst != sorted(lst):
        index = 0
        while index < len(lst)-1:
            if lst[index] > lst[index+1]:
                lst[index] = lst[index+1]
                lst[index + 1] = lst[index]
                swaps +=1
            index += 1
    return swaps

