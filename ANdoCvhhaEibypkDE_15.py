
def closing_in_sum(n):
    return sum_digits(str(n))
    
def sum_digits(n: str):
    if len(n) == 1:
        return int(n[0])
    if len(n) == 0:
        return 0
    num = int(n[0]+n[-1])
    return num + sum_digits(n[1:-1])

