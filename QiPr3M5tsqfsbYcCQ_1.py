
def square_digits(n):
    ans = ''
    for x in str(n):
        ans += str(int(x)**2)
    return int(ans)

