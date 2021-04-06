
def max_collatz(n):
    if n == 1: return 1
    col = []; i = n
    while i != 1:
        col.append(i)
        if i%2 == 0: i = int(i/2)
        else: i = i*3+1
    return max(col)

