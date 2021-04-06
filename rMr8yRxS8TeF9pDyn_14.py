
def war_of_numbers(lst):
    a = sorted([sum([i for i in lst if i % 2 == 0]), sum([i for i in lst if i % 2 != 0])])
    return a[1] - a[0]

