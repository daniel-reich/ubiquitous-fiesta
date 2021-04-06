
def quad_sequence(lst):
    diff = (lst[2]-lst[1]) - (lst[1]-lst[0])
    result = []
​
    curr = lst[-1]
    prev = lst[-2]
    for i in range(len(lst)):
        new = curr-prev+diff+curr
        prev = curr
        curr = new
        result.append(new)
​
    return result

