
def shuffle_count(num):
    n = [x+1 for x in range(num)]
​
    for c in range(num*num):
        n = [int(x) for x in str([x for x in zip(n[:round(len(n)/2)],n[round(len(n)/2):])]).replace("(","").replace(")","").replace("[","").replace("]","").split(', ')]
        if n == [x+1 for x in range(num)]:
            break
    return(c+1)

