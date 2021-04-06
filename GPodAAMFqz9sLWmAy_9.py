
def one_odd_one_even(n):
    return sum(1 for i in list(str(n)) if not int(i)%2)==1

