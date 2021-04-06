
def two_product(lst, n):
    for first_num in lst:
        for second_num in lst:
            if first_num * second_num == n and first_num != second_num:
                return sorted([first_num, second_num])

