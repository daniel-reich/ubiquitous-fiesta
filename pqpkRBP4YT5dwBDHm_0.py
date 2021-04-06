
def show_the_love(lst):
    new = [i * 0.75 for i in lst]
    new[lst.index(min(lst))] += sum(lst) - sum(new)
    return new

