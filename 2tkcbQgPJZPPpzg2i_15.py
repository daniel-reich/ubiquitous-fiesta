
def sum_of_holes(N):
    one = ['0', '4', '6', '9']
    str_range = ''.join(str(value) for value in range(1, N+1))
    return sum([str_range.count(n) * 1 for n in one] + [str_range.count('8') * 2])

