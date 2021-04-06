
def ranged_reversal(lst, start, finish):
    list1 = lst[start:finish+1][::-1]
    return lst[0:start] + list1 + lst[finish+1::]

