
def count_ones(lst):
    result = '0'+''.join([str(i) for i in lst])
    a = result.count('110')
    b = result.count('011')
    return max(a,b)

