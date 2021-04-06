
def triangle(perim, area):
    s = perim / 2
    result = []
    for a in range(1, int(perim / 3 + 1)):
        for b in range(a, int((perim - a) / 2 + 1)):
            c = perim - a - b
            # Heron squared
            h = s * (s-a) * (s-b) * (s-c)
            if h > 0 and round(h**0.5, 5) == area:
                result.append([a,b,c])
    return result

