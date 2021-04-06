
def gcd(lst):
    get_gcd = lambda x,y: x if y==0 else get_gcd(y, x%y)
    result = lst[0]
    for n in lst[1:]:
        result = get_gcd(result, n)
    return result

