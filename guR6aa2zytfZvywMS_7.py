
def total_overs(balls):
    x = divmod (balls,6)
    res = '.'.join(str(i) for i in x)
    return float (res)

