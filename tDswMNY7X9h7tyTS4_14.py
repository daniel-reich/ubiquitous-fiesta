
def pascals_triangle(n):
    p = [[1], [1,1]]
    if n == 1:
        return p[0]
        
    for _ in range(n-2):
        new_row = [1] + [a+b for a, b in zip(p[-1], p[-1][1:])] + [1]
        p.append(new_row)
    return sum(p, [])

