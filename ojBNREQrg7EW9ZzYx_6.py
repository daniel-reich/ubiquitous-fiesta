
valid = "-0123456789"
​
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    money = int(''.join([c for c in total_money if c in valid]))
    cost = int(''.join([c for c in cost_of_one_chocolate if c in valid]))
    if min(cost, money) <= 0:
        return "Invalid Input"
    choc = money // cost
    wrappers = choc
    while wrappers >= 3:
        new_choc = wrappers // 3
        choc += new_choc
        wrappers = wrappers % 3 + new_choc
    return choc

