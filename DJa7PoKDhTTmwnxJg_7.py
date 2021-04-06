
def adjacent_product(list1):
    return max(list1[i]*list1[i+1] for i in range(len(list1)-1))

