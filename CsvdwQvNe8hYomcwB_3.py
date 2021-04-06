
def remap(value, low1, high1, low2, high2):
    if not all((low1 - high1, low2 - high2)):
        return 0
    k = (high1 - value) / (high1 - low1)
    return high2 - (high2 - low2) * k

