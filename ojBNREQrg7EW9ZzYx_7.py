
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    m = int("".join([x for x in total_money if x.isnumeric()]))
    c = int("".join([y for y in cost_of_one_chocolate if y.isnumeric()]))
    if c == 0 or m == 0 or "-" in total_money or "-" in cost_of_one_chocolate:
        return "Invalid Input"
    r = m / c
    a, b = divmod(r, 3)
    while a > 0:
        r += a
        a, b = divmod(a + b, 3)
    return int(r)

