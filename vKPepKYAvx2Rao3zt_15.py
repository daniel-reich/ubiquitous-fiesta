
def car_timer(n):
    h, m = divmod(n, 60)
    return (sum(int(x) for x in str(h)) +
            sum(int(x) for x in str(m)))

