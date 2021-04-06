
def pascals_triangle(row):
    from math import factorial as f
    res = ""
    n = row
    for k in range(1,n):
        res += " " + str(int(f(n)/(f(k)*f(n-k)))) 
    return "1" + res + " 1"

