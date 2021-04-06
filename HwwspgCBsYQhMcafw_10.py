
def super_digit(n, k):
    if int(n) < 10:
        return int(n)
    while len(n) > 1:
        n = str(sum(eval(i) for i in n)) 
    return super_digit(str(int(n) * k),k = 1)

