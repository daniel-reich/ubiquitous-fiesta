
def sum_even_nums_in_range(start, stop):
    x = 0
    for i in range(start, stop + 1):
        if i % 2 == 0:
            x += i
    return x
​
​
print(sum_even_nums_in_range(10, 20))

