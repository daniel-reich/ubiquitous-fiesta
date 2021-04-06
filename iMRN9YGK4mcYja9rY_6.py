
def accumulating_product(lst):
    result = []
    for i in range(0, len(lst)):
        listSlice = lst[0:i+1]
        result.append(multiplyList(listSlice))
    return result
​
def multiplyList(lst):
    total = 1
    for number in lst:
        total *= number
    return total

