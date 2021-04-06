
def car_timer(n):
    n = n * 60
    Hours = ((n % (24 * 3600)) // 3600)
    n %= 3600
    Minutes = ((n % (24 * 3600 * 3600)) // 60)
    ans = (list(str(Hours)+str(Minutes)))
    return sum(list(map(lambda x:int(x),ans)))

