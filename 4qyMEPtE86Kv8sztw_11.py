
def binary_num_convert(num):
    num_lst = num.split(".")
    total_1 = 0
    total_2 = 0
    for i in range(len(num_lst[0])):
        total_1 += int(num_lst[0][i]) * ( 2 ** (len(num_lst[0]) - 1 - i))
    for i in range(len(num_lst[1])):
        total_2 += float(int(num_lst[1][i]) * (1/ (2 ** (i +1))))
    return total_1 + total_2
​
def decimal_convert(num):
    i = 0
    while int(num * (2 ** i)) != num * ( 2** i):
        i += 1
    return str(int(num * (2 ** i))) + "/" + str(2 ** i)
​
​
def binary_sum(lst):
    total = 0
    for num in lst:
        total += binary_num_convert(num)
    if int(total) == total:
        return str(int(total))
    elif total < 1:
        return str(decimal_convert(total))
    elif total >=1:
        return str(int(total)) + " " + decimal_convert(total-int(total))

