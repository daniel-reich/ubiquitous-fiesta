
def triangle(p, A):
    '''
    Returns a list of lists [a,b,c] where a, b and c are sides of a triangle
    in increasing order such that a+b+c = p and the triangle's area = A
    '''
    TOL = 0.00001  # tolerance on area checks
    triangles = []
    s = p / 2
​
    for a in range(1, p//3 + 1):
        for b in range(1, (p-a)//2 + 1):
            c = p - a - b
            area = (s * (s - a) * (s - b) * (s - c)) **0.5
            if abs(A - area) <= TOL:
                t = sorted([a, b, c])
                if t not in triangles:
                    triangles.append(t)
​
    return triangles

