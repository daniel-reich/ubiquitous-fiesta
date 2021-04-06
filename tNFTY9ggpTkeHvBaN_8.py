
def total_volume(*args):
    sum = 0
    for each_list in args:
        mul=1
        for num in each_list:
            mul = mul*num
        sum = sum + mul
    return sum

