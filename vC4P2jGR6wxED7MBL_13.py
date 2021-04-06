
def larger_than_right(lst):
    return [lst[j] for j in range(len(lst)-1) if lst[j] > max(lst[j+1:])] + [lst[-1]]

