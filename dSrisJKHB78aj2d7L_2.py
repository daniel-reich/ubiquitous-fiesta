
def triangle(peri, area):
    def heron(a, b, c):
        s = (a + b + c) / 2
        aa = (s * (s - a) * (s - b) * (s - c))
        if aa > 0:
            return round(aa**.5, 5)
​
    valid_triangles = []
    for s1 in range(1, peri // 2 + 1):
        for s2 in range(1, peri - s1):
            s3 = peri - s1 - s2
            if heron(s1, s2, s3) == area:
                valid_triangle = sorted([s1, s2, s3])
                if valid_triangle not in valid_triangles:
                    valid_triangles.append(valid_triangle)
    return valid_triangles

