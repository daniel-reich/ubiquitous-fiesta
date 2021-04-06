
def is_narcissistic(n):
    S = 0
    N= n
    while n > 0:
        i = n%10
        S = S + i**int(len(str(N)))
        n = n//10
    return True if S == N else False

