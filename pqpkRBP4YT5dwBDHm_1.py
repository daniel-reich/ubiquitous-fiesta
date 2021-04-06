
def show_the_love(lst):
    smallest = min(lst)
    add_on = (sum(lst) - smallest) * 0.25
    return [k + add_on if k == smallest else k * 0.75 for k in lst]

