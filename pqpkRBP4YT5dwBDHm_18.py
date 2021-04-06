
def show_the_love(lst):
    total = 0
    smallest = lst[0]
    new_list = []
    
    for num in lst:
        rem = num * 0.25
        total += rem
        num -= rem
        new_list.append(num)
    
    lowest = min(new_list)
    index = new_list.index(lowest)
    new_list[index] += total
    
    return new_list

