
def remap(value, low1, high1, low2, high2):
    if high1 == low1:
        return 0
    return (((high2 - low2)/(high1 - low1)) * (value - low1)) + low2

