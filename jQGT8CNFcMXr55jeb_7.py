
def numbers_sum(lst):
    sum = 0
    for num in lst:
       if type(num) == int:
           sum += num
    return sum

