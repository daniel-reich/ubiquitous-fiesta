
def herons_2(a, b, c):
    s = (a + b + c) / 2
    return s * (s-a) * (s-b) * (s-c)
​
def triangle(perimeter, area):
    area_2 = area ** 2
    margin = 0.001
    all_sides = set()
    for i in range(perimeter - 2, 0, -1):
        for j in range(perimeter - i - 1, 0, -1):
            k = perimeter - i - j
            if abs(herons_2(i, j, k) - area_2) < margin:
                all_sides.add(tuple(sorted((i, j, k))))
    return [list(s) for s in sorted(all_sides)]

