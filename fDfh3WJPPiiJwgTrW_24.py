
def num_of_sublists(lst):
    x = 0
    for i in lst:
        if type(i) == list:
            x += 1
    return x
num_of_sublists([[1],[1,4,5],[1,7,'a',3], 7, 5, 3 , [54, 2]])

