
def get_products(lst):
    result = []
    for i in lst:
        lst2 = lst[0:]
        lst2.remove(i)
        total, count = lst2[0], 0
        while count < len(lst2) - 1:
            total = total * lst2[count+1]
            count += 1
        result.append(total)
    return result

