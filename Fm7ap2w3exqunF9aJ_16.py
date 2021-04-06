
def count_lone_ones(n):
    str1 = str(n)
    lst1 = [i * '1' for i in range(2, len(str1) + 1)]
    for i in lst1[::-1]: str1 = str1.replace(i, '')
    return list(str1).count('1')

