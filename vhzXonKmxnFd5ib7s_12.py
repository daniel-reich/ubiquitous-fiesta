
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
​
def matrix_multiply(a, b):
    if len(a[0]) != len(b): return 'invalid'
    return [[sum(ar[i] * bc[i] for i in range(len(ar))) for bc in rotate_matrix(b)] for ar in a]

