
def range_of_num(a, b):
    numbers = []
    if a == b:
        return numbers
    else:
        while a + 1 != b:
            a = a + 1
            numbers.append(a)
        return numbers

