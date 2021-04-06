
def difference_two(lst):
    result = []
    lst.sort()
    for num1 in lst:
        for num2 in lst:
            if abs(num1-num2)==2 and sorted([num1,num2]) not in result:
                result.append([num1,num2])
    return result

