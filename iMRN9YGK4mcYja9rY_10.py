
def accumulating_product(lst):
    other = []
    for i in range(len(lst)):
        if i == 0:
            other.append(lst[0])
        else:
            prod = lst[:i+1]
            val = 1
            for j in prod:
                val*=j
            other.append(val)
    return (other)

