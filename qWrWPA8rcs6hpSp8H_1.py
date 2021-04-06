
def determinant(A):
    d = len(A)
    if d == 1:
        return A[0][0]
    elif d == 2:
        return A[1][1]*A[0][0]-A[1][0]*A[0][1]
    else:
        sum = 0
        for i in range(d):
            if i == 0:
                sum += A[0][i]*determinant([j[1:] for j in A[1:]])
            elif i == d:
                sum += A[0][i]*determinant([j[:-1] for j in A[1:]])*(1-2*(i%2))
            else:
                sum += A[0][i]*determinant([j[:i]+j[i+1:]for j in A[1:]])*(1-2*(i%2))
        return sum

