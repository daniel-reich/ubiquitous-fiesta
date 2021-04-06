
def max_product(n):
    prod, numb, ans = [], [], []
    for each in range(1, n + 1):
        i = 1
        for num in str(each):
            i *= int(num)
        numb.append(each)
        prod.append(i)
    for each in range(prod.count(max(prod))):
        get_index = prod.index(max(prod))
        ans.append(numb[get_index])
        prod.remove(max(prod))
        numb.remove(numb[get_index])
    return ans

