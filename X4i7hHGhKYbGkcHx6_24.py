
def average_index(letters):
    z = [1+ord(x)-ord('a') for x in letters]
    return round(sum(z) / len(z), 2)

