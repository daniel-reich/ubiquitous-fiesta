
def add_digits(temp_list):
    result = 0
    for num in temp_list:
        result += int(num)
    return result
​
def is_equal(lst):
    return add_digits(list(str(lst[0]))) == add_digits(list(str(lst[1])))

